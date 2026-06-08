# utils/roi.py

def calculate_roi(avg_package, annual_fee):
    # Scale annual fee to 4-year cumulative cost for accurate ratio processing
    total_fee_4_years = annual_fee * 4
    if total_fee_4_years == 0: 
        return 10.0, "High"
    
    roi = round(avg_package / total_fee_4_years, 2)
    
    # Strictly re-mapped labels to output only Low, Medium, or High as per criteria
    if roi >= 1.3:
        label = "High"
    elif roi >= 1.0:
        label = "Medium"
    else:
        label = "Low"
        
    return roi, label


def get_roi_analysis(college):
    avg_package = college["avg_package"]
    annual_fee = college["total_fee"]
    hostel_fee = college["hostel_fee"]
    
    # Calculate total 4-year degree outlay correctly
    total_cost = round((annual_fee * 4) + (hostel_fee * 4), 2)
    roi_score, roi_label = calculate_roi(avg_package, annual_fee)
    
    payback = round(total_cost / avg_package, 1) if avg_package > 0 else 0
    return {
        "roi_score": roi_score, 
        "roi_label": roi_label, # Returns strictly Low, Medium, or High
        "total_cost": total_cost, 
        "payback_years": payback,
    }


def overall_score(admission_pct, avg_pkg, roi, infra, accred):
    return round(
        (admission_pct / 100) * 10 * 0.35 +
        min(10, avg_pkg / 2) * 0.30 +
        min(10, roi * 3) * 0.15 +
        infra * 0.10 +
        accred * 0.10, 2)
