# utils/recommender.py
from data.colleges import COLLEGES
from utils.predictor import predict_admission, get_predicted_2026_cutoff
from utils.roi import calculate_roi, get_roi_analysis, overall_score

def get_recommendations(rank, category, branch, budget, location, hostel):
    results = []
    for c in COLLEGES:
        if branch not in c["branches"]: 
            continue
        if c["total_fee"] > budget: 
            continue
        if hostel and not c["hostel"]: 
            continue
        if location != "Any" and c["location"] != location: 
            continue

        label, pct = predict_admission(rank, category, c, branch)
        if pct < 5: 
            continue

        roi_score, roi_label = calculate_roi(c["avg_package"], c["total_fee"])
        roi_data = get_roi_analysis(c)
        score = overall_score(pct, c["avg_package"], roi_score,
                              c["infrastructure"], c["accreditation"])

        tier = ("Backup" if pct >= 80 else "Safe" if pct >= 55
                else "Target" if pct >= 30 else "Dream")

        results.append({
            "name": c["name"], 
            "full_name": c["full_name"],
            "branch": branch, 
            "type": tier,
            "chance_label": label, 
            "chance_pct": pct,
            "avg_package": c["avg_package"],
            "highest_package": c["highest_package"],
            "placement_pct": c["placement_pct"],
            "total_fee": c["total_fee"],
            "hostel": c["hostel"], 
            "hostel_fee": c["hostel_fee"],
            "roi": roi_label, # Directly maps High, Medium, Low
            "roi_score": roi_score, 
            "roi_data": roi_data,
            "infrastructure": c["infrastructure"],
            "accreditation": c["accreditation"],
            "naac": c["naac"], 
            "location": c["location"],
            "college_type": c["type"],
            "companies": c["companies"], 
            "about": c["about"],
            "overall_score": score,
        })
        
    results.sort(key=lambda x: x["overall_score"], reverse=True)
    return results
