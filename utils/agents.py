# utils/agents.py
from utils.predictor import predict_admission, get_predicted_2026_cutoff
from utils.roi import get_roi_analysis


def run_all_agents(college, rank, category, preferred_location):
    # Defaulting branch to "CSE" for global scorecard view if not explicitly provided
    target_branch = "CSE" 

    # 1. Placement Agent
    pkg_score = min(10, college["avg_package"] / 2)
    placement = {
        "score": round(pkg_score, 1),
        "avg_package": college["avg_package"],
        "highest_package": college["highest_package"],
        "placement_pct": college["placement_pct"],
        "companies": college["companies"],
        "verdict": "Excellent" if pkg_score >= 8 else "Good" if pkg_score >= 6 else "Average"
    }

    # 2. Cutoff Agent (Updated to handle branch context for multi-year tracking)
    label, pct = predict_admission(rank, category, college, target_branch)
    predicted_cutoff = get_predicted_2026_cutoff(college, category, target_branch)
    cutoff_data = {
        "score": round(pct / 10, 1),
        "cutoff": predicted_cutoff,
        "your_rank": rank,
        "chance_label": label,
        "chance_pct": pct,
        "verdict": label
    }

    # 3. ROI Agent
    roi = get_roi_analysis(college)
    roi_score = min(10, roi["roi_score"] * 3)
    roi_data = {
        "score": round(roi_score, 1),
        "roi_score": roi["roi_score"],
        "roi_label": roi["roi_label"],
        "total_cost": roi["total_cost"],
        "payback_years": roi["payback_years"],
        "verdict": "Excellent" if roi_score >= 7 else "Good" if roi_score >= 5 else "Average"
    }

    # 4. Accreditation Agent
    naac_map = {"A++": 10, "A+": 9, "A": 8, "B++": 7, "B+": 6, "B": 5}
    acc_score = naac_map.get(college["naac"], 5)
    accred = {
        "score": acc_score,
        "naac": college["naac"],
        "type": college["type"],
        "verdict": "Top Tier" if acc_score >= 9 else "Good" if acc_score >= 7 else "Average"
    }

    # 5. Hostel Agent
    if not college["hostel"]:
        hostel = {"score": 4, "available": False, "fee": 0, "verdict": "Not Available"}
    else:
        fee = college["hostel_fee"]
        h_score = 9 if fee <= 0.8 else 8 if fee <= 1.0 else 7
        hostel = {"score": h_score, "available": True, "fee": fee,
                  "verdict": "Affordable" if fee <= 0.8 else "Moderate" if fee <= 1.2 else "Expensive"}

    # 6. Location Agent
    if preferred_location == "Any" or college["location"] == preferred_location:
        loc = {"score": 9, "college_location": college["location"],
               "preferred": preferred_location, "verdict": "Perfect Match"}
    else:
        loc = {"score": 6, "college_location": college["location"],
               "preferred": preferred_location, "verdict": "Different City"}

    # Final Combined Scoring Core Weights
    final = round(
        placement["score"] * 0.35 + cutoff_data["score"] * 0.30 +
        roi_data["score"] * 0.15 + accred["score"] * 0.10 +
        hostel["score"] * 0.05 + loc["score"] * 0.05, 2)

    return {
        "college_name": college["name"],
        "placement": placement, 
        "cutoff": cutoff_data,
        "roi": roi_data, 
        "accreditation": accred,
        "hostel": hostel, 
        "location": loc,
        "final_score": final,
    }
