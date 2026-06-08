# predictor.py

def get_predicted_2026_cutoff(college, category, branch="CSE"):
    branch_map = college.get("branches", {}).get(branch, {})
    if not branch_map:
        return 50000  # Default safe margin string fallback

    # Extract 5-year baseline history array [2021, 2022, 2023, 2024, 2025]
    history = branch_map["history"]
    
    # Apply a weighted moving average forecasting formula (Recent years hold higher weight)
    weights = [0.05, 0.10, 0.15, 0.30, 0.40]
    gm_predicted = sum(h * w for h, w in zip(history, weights))
    
    # Calculate relaxation multiplier adjustments for individual reservation quotas
    category_multiplier = {
        "GM": 1.0,
        "OBC": 1.35,
        "SC": 2.5,
        "ST": 2.8
    }.get(category, 1.0)
    
    return round(gm_predicted * category_multiplier)


def predict_admission(rank, category, college, branch="CSE"):
    predicted_cutoff = get_predicted_2026_cutoff(college, category, branch)
    diff = predicted_cutoff - rank
    
    if diff > 15000: return "Very High", 95
    elif diff > 8000: return "High", 78
    elif diff > 3000: return "Moderate", 52
    elif diff > 0:    return "Low", 28
    else:             return "Very Low", 8


def get_profile_score(rank, category, branch, budget, location, hostel):
    rank_score    = max(0, min(100, 100 - (rank / 1500)))
    cat_score     = min(100, {"GM": 40, "OBC": 55, "SC": 70, "ST": 80}.get(category, 40))
    branch_score  = {"CSE": 90, "ISE": 85, "AIML": 80, "ECE": 75}.get(branch, 70)
    budget_score  = min(100, budget * 6)
    loc_score     = {"Bangalore": 60, "Mysore": 75, "Tumkur": 85, "Any": 70}.get(location, 70)
    hostel_score  = 80 if hostel else 90
    
    total = (rank_score * 0.40 + cat_score * 0.20 + branch_score * 0.15 +
             budget_score * 0.05 + loc_score * 0.10 + hostel_score * 0.10)
    return {
        "total": round(total),
        "rank_score": round(rank_score),
        "cat_score": round(cat_score),
        "branch_score": round(branch_score),
        "budget_score": round(budget_score),
        "loc_score": round(loc_score),
        "hostel_score": round(hostel_score),
        "competition": "High" if rank < 12000 else "Moderate" if rank < 40000 else "Low",
    }
