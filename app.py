# app.py
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

from data.colleges import COLLEGES
from utils.predictor import predict_admission, get_profile_score, get_predicted_2026_cutoff
from utils.roi import get_roi_analysis, calculate_roi, overall_score
from utils.recommender import get_recommendations
from utils.agents import run_all_agents
from utils.chatbot import get_chat_response

# Dynamically pull max limits straight from the colleges dataset
MAX_ANNUAL_FEE_CEILING = float(max(c["total_fee"] for c in COLLEGES))

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="SmartCET AI Counselor",
    page_icon="🎓",
    layout="wide"
)

# Global custom HTML/CSS styling layers (Slate Grey & Tech Blue Theme)
st.markdown("""
    <style>
    .main { background-color: #F4F6F9; }
    .metric-card {
        background-color: white; padding: 20px; border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center;
    }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 20px; background-color: #E2E5E9; border-radius: 5px;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: #007BFF; color: white;
    }
    
    /* ── PERSISTENT GLOBAL TOP-RIGHT CORNER ICON LAYOUT CONTAINER ── */
    .aveon-top-icon-container {
        position: fixed;
        top: 60px;
        right: 25px;
        z-index: 999999;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar clean navigation layout
navigation_target = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Home",
        "👤 Student Profile",
        "🏫 College Recommendations",
        "🎯 Admission Predictor",
        "🤖 AI Counselor",
        "📊 Analytics",
        "💰 ROI Analyzer",
        "🔬 College Scorecard",
    ]
)

# Persistent Sidebar Profile Status
if "rank" in st.session_state and st.session_state["rank"] is not None:
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Your Active Profile**")
    st.sidebar.write(f"Rank: {st.session_state['rank']:,}")
    st.sidebar.write(f"Category: {st.session_state['category']}")
    st.sidebar.write(f"Branch Pref: {st.session_state['branch']}")

# Initialize States
if "aveon_popup_active" not in st.session_state:
    st.session_state["aveon_popup_active"] = False
if "aveon_messages" not in st.session_state:
    st.session_state.aveon_messages = []

# ══════════════════════════════════════════════════════════════════════════════
# 🤖 PERSISTENT GLOBAL BOT ENGINES (RUNS ON EVERY PAGE EXCLUDING "🤖 AI Counselor")
# ══════════════════════════════════════════════════════════════════════════════
if navigation_target != "🤖 AI Counselor":
    st.markdown('<div class="aveon-top-icon-container">', unsafe_allow_html=True)
    
    col_icon1, col_icon2 = st.columns([12, 2.2])
    with col_icon2:
        if not st.session_state["aveon_popup_active"]:
            if st.button("🤖 Open Aveon Bot", help="Click to display input bar at bottom", use_container_width=True):
                st.session_state["aveon_popup_active"] = True
                st.rerun()
        else:
            if st.button("✖️ Close Aveon Bot", help="Hide input bar from bottom view", use_container_width=True):
                st.session_state["aveon_popup_active"] = False
                st.rerun()
                
    st.markdown('</div>', unsafe_allow_html=True)

    # Triggering the fluid bottom-docked chat input when active
    if st.session_state["aveon_popup_active"]:
        if user_query := st.chat_input("Type your question here for Aveon AI and press Enter...", key="global_bottom_aveon_input"):
            st.session_state.aveon_messages.append({"role": "user", "content": user_query})
            with st.spinner("Processing matching pathways..."):
                reply_text = get_chat_response(st.session_state.aveon_messages)
            st.session_state.aveon_messages.append({"role": "assistant", "content": reply_text})
            
            # Displays the response as a clean toast popup banner
            st.toast(f"🤖 Aveon AI: {reply_text}", icon="🤖")

# ══════════════════════════════════════════════════════════════════════════════
# 🏠 HOME VIEW
# ══════════════════════════════════════════════════════════════════════════════
if navigation_target == "🏠 Home":
    st.title("🎓 SmartCET AI Counselor")
    st.subheader("Karnataka CET College Admission Platform — Powered by AI")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Verified KEA Institutions", str(len(COLLEGES)))
    c2.metric("AI Analytical Engines", "7")
    c3.metric("Supported Quotas", "GM, OBC, SC, ST")
    c4.metric("Core AI LLM", "Groq LLaMA3")

    st.markdown("---")
    st.markdown("""
| Platform Feature | Analytical Capability |
|------------------|----------------------|
| 👤 Student Profile | Evaluates rank metrics, score weightings, and maps radial radar layouts. |
| 🏫 Recommendations | Constructs tiered strategy pathways segmented from Dream to Backup options. |
| 🎯 Admission Predictor | Computes trend probabilities across multiple branches simultaneously. |
| 🤖 AI Counselor | Answers custom KEA compliance, fee, and facility verification questions via Groq. |
| 📊 Analytics | Compares cross-platform trends, mass recruitment stats, and geographic cluster filters. |
| 💰 ROI Analyzer | Measures direct academic outlay against multi-year payback horizons. |
| 🔬 College Scorecard | Features 5-Year historical tracking charts, 2026 predictions, and live website links. |
""")
    st.info("👈 Initialize your entry vectors by selecting **Student Profile** in the sidebar navigation menu!")

# ══════════════════════════════════════════════════════════════════════════════
# 👤 STUDENT PROFILE ANALYZER
# ══════════════════════════════════════════════════════════════════════════════
elif navigation_target == "👤 Student Profile":
    st.title("👤 Student Profile Analyzer")
    st.caption("Establish baseline student parameters to activate background predictive models.")

    with st.form("profile_form"):
        c1, c2 = st.columns(2)
        with c1:
            rank = st.number_input("KEA CET Rank", min_value=1, max_value=300000, value=None, placeholder="Type your CET Rank here...")
            category = st.selectbox("Reservation Category Quota", [None, "GM", "OBC", "SC", "ST"], index=0, format_func=lambda x: "Choose Quota..." if x is None else x)
            branch = st.selectbox("Preferred Discipline Focus", [None, "CSE", "ISE", "AIML", "ECE"], index=0, format_func=lambda x: "Choose Engineering Branch..." if x is None else x)
        with c2:
            budget = st.slider("Max Annual Fee Budget Threshold (Lakhs ₹ / Year)", min_value=0.2, max_value=MAX_ANNUAL_FEE_CEILING, value=float(MAX_ANNUAL_FEE_CEILING), step=0.01, format="%.2f L")
            location = st.selectbox("Preferred Geographic Hub Location", [None, "Any", "Bangalore", "Mysore", "Hubli", "Dharwad", "Tumkur"], index=0, format_func=lambda x: "Choose Location..." if x is None else x)
            hostel = st.radio("Require On-Campus Housing Accommodations?", [None, "Yes", "No"], index=0, format_func=lambda x: "Select Preference..." if x is None else x)
            
        submitted = st.form_submit_button("🔍 Analyze Profile Matrix", use_container_width=True)

    if submitted:
        if rank is None or category is None or branch is None or location is None or hostel is None:
            st.error("❌ Please make selections for all fields. No default options are provided.")
        else:
            hostel_bool = (hostel == "Yes")
            st.session_state.update({
                "rank": rank, "category": category, "branch": branch,
                "budget": budget, "location": location, "hostel": hostel_bool
            })
            p = get_profile_score(rank, category, branch, budget, location, hostel_bool)

            st.success("✅ Student credentials registered successfully across global pipeline layers!")
            c1, c2, c3 = st.columns(3)
            c1.metric("Comprehensive Profile Score", f"{p['total']}/100")
            c2.metric("Competition Grid Index", p["competition"])
            c3.metric("Target Academic Stream", branch)

            st.markdown("---")
            factors = ["Rank Strength", "Category Advantage", "Branch Demand", "Budget Match", "Location Score", "Hostel Pref"]
            values  = [p["rank_score"], p["cat_score"], p["branch_score"], p["budget_score"], p["loc_score"], p["hostel_score"]]

            c1, c2 = st.columns(2)
            with c1:
                fig = go.Figure(go.Scatterpolar(
                    r=values + [values[0]], theta=factors + [factors[0]],
                    fill='toself', line_color='royalblue',
                    fillcolor='rgba(65,105,225,0.25)'
                ))
                fig.update_layout(polar=dict(radialaxis=dict(range=[0, 100])), title="Profile Strength Radar Plot", height=400)
                st.plotly_chart(fig, use_container_width=True)

            with c2:
                fig2 = px.bar(x=factors, y=values, color=values, color_continuous_scale="blues",
                              title="Factor Score Breakdown Weights", labels={"x": "Evaluated Metric Vectors", "y": "Normalized Index Score"})
                fig2.update_layout(height=400)
                st.plotly_chart(fig2, use_container_width=True)

# ══════════════════════════════════════════════════════════════════════════════
# 🏫 COLLEGE RECOMMENDATION ENGINE
# ══════════════════════════════════════════════════════════════════════════════
elif navigation_target == "🏫 College Recommendations":
    st.title("🏫 Strategic Tiered College Recommendation Engine")

    if "rank" not in st.session_state or st.session_state["rank"] is None:
        st.warning("⚠️ Profile parameters uninitialized. Configure variables in **Student Profile** analyzer view first.")
        st.stop()

    rank     = st.session_state["rank"]
    category = st.session_state["category"]
    branch   = st.session_state["branch"]
    budget   = st.session_state["budget"]
    location = st.session_state["location"]
    hostel   = st.session_state["hostel"]

    st.info(f"Targeting Matrix Filters: Rank **{rank:,}** | Quota: **{category}** | Discipline: **{branch}** | Max Annual Fees Allowed: **₹{budget:.2f}L/Year**")

    results = get_recommendations(rank, category, branch, budget, location, hostel)

    if not results:
        st.error("No institutions matched your explicit boundary constraints. Try expanding your annual fee budget slider slightly.")
        st.stop()

    dream  = [c for c in results if c["type"] == "Dream"]
    target = [c for c in results if c["type"] == "Target"]
    safe   = [c for c in results if c["type"] == "Safe"]
    backup = [c for c in results if c["type"] == "Backup"]

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("🔴 Dream Institutions", len(dream))
    c2.metric("🟡 Target Options", len(target))
    c3.metric("🟢 Safe Horizons", len(safe))
    c4.metric("⚪ Backup Options", len(backup))
    st.markdown("---")

    icons = {"Dream": "🔴", "Target": "🟡", "Safe": "🟢", "Backup": "⚪"}
    for tier in ["Dream", "Target", "Safe", "Backup"]:
        tier_list = [c for c in results if c["type"] == tier]
        if not tier_list: continue
        st.subheader(f"{icons[tier]} {tier} Strategic Pathways")
        for c in tier_list:
            with st.expander(f"**{c['name']}** | Admission Chances: **{c['chance_label']}** ({c['chance_pct']}%) | Combined Pipeline Weight: **{c['overall_score']}/10**"):
                r1, r2, r3, r4 = st.columns(4)
                r1.metric("Average Income", f"{c['avg_package']} LPA")
                r2.metric("Annual KEA Fees", f"₹{c['total_fee']:.2f} Lakhs/Yr")
                r3.metric("Return Metric", c['roi'])
                r4.metric("Corporate Placement %", f"{c['placement_pct']}%")
                
                r5, r6, r7, r8 = st.columns(4)
                r5.metric("NAAC Grade", c['naac'])
                r6.metric("Geographic Location", c['location'])
                r7.metric("Hostel Facility", "✅ Available" if c['hostel'] else "❌ Unavailable")
                r8.metric("Regulatory Status", c['college_type'])
                
                st.caption(f"🏢 **Top Visiting Placement Partners:** {', '.join(c['companies'])}")
                st.caption(f"ℹ️ **Background Context:** {c['about']}")

    st.markdown("---")
    st.subheader("📊 Strategic Optimization Visualization Map")
    df = pd.DataFrame(results)
    
    fig = px.scatter(
        df, x="total_fee", y="avg_package", size="chance_pct", color="type", text="name",
        labels={"total_fee": "KEA Annual Fees (Lakhs ₹)", "avg_package": "Average Placements (LPA)", "type": "Strategic Tier"},
        title="Tuition Cost vs Compensation Metrics Map",
        color_discrete_map={"Dream": "#dc3545", "Target": "#ffc107", "Safe": "#28a745", "Backup": "#6c757d"},
        size_max=30
    )
    fig.update_traces(textposition='top center', cliponaxis=False)
    fig.update_layout(hovermode="closest", legend=dict(bgcolor="rgba(255,255,255,0.8)"))
    st.plotly_chart(fig, use_container_width=True)

# ══════════════════════════════════════════════════════════════════════════════
# 🎯 ADMISSION PROBABILITY PREDICTOR
# ══════════════════════════════════════════════════════════════════════════════
elif navigation_target == "🎯 Admission Predictor":
    st.title("🎯 Multi-Branch Entry Predictor")

    if "rank" not in st.session_state or st.session_state["rank"] is None:
        st.warning("⚠️ Profile parameters missing. Initialize vectors via **Student Profile** menu tab.")
        st.stop()

    rank     = st.session_state["rank"]
    category = st.session_state["category"]
    st.info(f"Active Profile Evaluator: Rank **{rank:,}** | Category Allotment: **{category}**")

    rows = []
    for c in COLLEGES:
        for b_name in c["branches"].keys():
            label, pct = predict_admission(rank, category, c, b_name)
            predicted_cutoff = get_predicted_2026_cutoff(c, category, b_name)
            rows.append({
                "Institution": c["name"],
                "Engineering Discipline": b_name,
                "Projected 2026 Cutoff Bound": f"{predicted_cutoff:,} Ranks",
                "Your Merit Vector": f"{rank:,} Ranks",
                "Probability Metric": label,
                "Odds Score %": pct,
                "Average Placement": f"{c['avg_package']} LPA",
                "Annual Fee": f"₹{c['total_fee']:.2f}L/Yr"
            })

    df = pd.DataFrame(rows).sort_values("Odds Score %", ascending=False)

    def color_pred(val):
        return {
            "Very High": "background-color:#d4edda; color:#155724;",
            "High":      "background-color:#d1ecf1; color:#0c5460;",
            "Moderate":  "background-color:#fff3cd; color:#856404;",
            "Low":       "background-color:#f8d7da; color:#721c24;",
            "Very Low":  "background-color:#f5c6cb; color:#721c24;",
        }.get(val, "")

    st.write("### Complete System-Wide Probability Ledger")
    st.dataframe(df.style.map(color_pred, subset=["Probability Metric"]), use_container_width=True, hide_index=True)

# ══════════════════════════════════════════════════════════════════════════════
# 🤖 DEDICATED AI COUNSELOR CHATBOT HUB (BOT BUTTON WILL DISAPPEAR ON THIS VIEW)
# ══════════════════════════════════════════════════════════════════════════════
elif navigation_target == "🤖 AI Counselor":
    st.title("🤖 Dedicated AI Counselor Chatbot Hub")
    st.caption("Semantic Conversational Admissions Intelligence Layer Powered by Groq LLaMA3.1")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if not st.session_state.messages:
        st.markdown("### 💡 Recommended System Queries")
        suggestions = [
            "Compare RVCE vs NCET placements across CSE and ISE tracks.",
            "What safe options do I have around a rank of 25k under GM quota?",
            "Is Nagarjuna College of Engineering (NCET) a solid choice for AIML infrastructure?",
            "Which colleges show the absolute best Return on Investment curves under ₹1.15 Lakhs annual fee?",
            "List top autonomous engineering branches matching an ISE priority choice."
        ]
        cols = st.columns(2)
        for i, s in enumerate(suggestions):
            if cols[i % 2].button(s, use_container_width=True):
                st.session_state.messages.append({"role": "user", "content": s})
                with st.spinner("Processing knowledge graphs..."):
                    reply = get_chat_response(st.session_state.messages)
                st.session_state.messages.append({"role": "assistant", "content": reply})
                st.rerun()

    if prompt := st.chat_input("Input custom admission questions...", key="dedicated_counselor_input"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        with st.chat_message("assistant"):
            with st.spinner("Analyzing parameters..."):
                reply = get_chat_response(st.session_state.messages)
            st.write(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})

    if st.session_state.messages:
        if st.button("🗑️ Reset Chat History", use_container_width=True):
            st.session_state.messages = []
            st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
# 📊 ANALYTICS DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════
elif navigation_target == "📊 Analytics":
    st.title("📊 Structural Analytics Dashboard")

    df = pd.DataFrame(COLLEGES)
    df["roi_score"] = (df["avg_package"] / (df["total_fee"] * 4)).round(2)

    c1, c2 = st.columns(2)
    with c1:
        fig = px.bar(df.sort_values("avg_package", ascending=False), x="name", y="avg_package", color="naac",
                     labels={"name": "College Name", "avg_package": "Avg Salary (LPA)"},
                     title="🏆 Average Packages Across Institutions (LPA)", text="avg_package")
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        fig2 = px.pie(df, names="location", title="🗺️ Geographic Allotment Density Maps", hole=0.3)
        st.plotly_chart(fig2, use_container_width=True)

# ══════════════════════════════════════════════════════════════════════════════
# 💰 ROI ANALYZER
# ══════════════════════════════════════════════════════════════════════════════
elif navigation_target == "💰 ROI Analyzer":
    st.title("💰 Capital Efficiency & ROI Analyzer")

    rows = []
    for c in COLLEGES:
        r = get_roi_analysis(c)
        rows.append({
            "College": c["name"],
            "Average Comp (LPA)": c["avg_package"],
            "Highest Pack": c["highest_package"],
            "Placement %": c["placement_pct"],
            "Annual KEA Quota Fee": f"₹{c['total_fee']:.2f} L/Yr",
            "Total 4-Yr Degree Outlay": r["total_cost"],
            "ROI Score (Multiplier)": r["roi_score"],
            "Efficiency Category": r["roi_label"],
            "Payback Period (Years)": r["payback_years"]
        })

    df = pd.DataFrame(rows).sort_values("ROI Score (Multiplier)", ascending=False)
    st.dataframe(df, use_container_width=True, hide_index=True)

# ══════════════════════════════════════════════════════════════════════════════
# 🔬 MULTI-YEAR SCORECARD HUB
# ══════════════════════════════════════════════════════════════════════════════
elif navigation_target == "🔬 College Scorecard":
    st.title("🔬 Multi-Year Analytical College Scorecard")
    st.caption("Historical closing trend logic mapping precisely which discipline choices align with your merit standing.")

    if "rank" in st.session_state and st.session_state["rank"] is not None:
        user_rank = st.session_state["rank"]
        user_category = st.session_state["category"]
        user_branch = st.session_state["branch"]
        user_budget = st.session_state["budget"]
        user_location = st.session_state["location"]
        user_hostel = st.session_state["hostel"]
        st.info(f"Using Active Profile: Rank {user_rank:,} | {user_category} Quota | Branch Focus: {user_branch}")
    else:
        st.warning("⚠️ For a fully optimized analysis, please configure your criteria inside the 'Student Profile' tab first.")
        c_setup1, c_setup2 = st.columns(2)
        with c_setup1:
            user_rank = st.number_input("Enter your CET Merit Rank:", min_value=1, max_value=300000, value=18500)
            user_category = st.selectbox("Select Target Quota Category:", ["GM", "OBC", "SC", "ST"])
            user_branch = st.selectbox("Select Branch Focus:", ["CSE", "ISE", "AIML", "ECE"])
        with c_setup2:
            user_budget = st.slider("Max Annual Fee (Lakhs ₹/Yr):", min_value=0.2, max_value=1.5, value=1.2)
            user_location = st.selectbox("Preferred Location Hub:", ["Any", "Bangalore", "Mysore", "Hubli"])
            user_hostel = st.checkbox("Require On-Campus Hostel Accommodation", value=True)

    st.markdown("---")
    
    selected_college_name = st.selectbox("Select an institution to inspect:", [c["name"] for c in COLLEGES])
    college_record = next(c for c in COLLEGES if c["name"] == selected_college_name)

    st.markdown(f"## 🏫 {college_record['full_name']}")
    
    col_meta1, col_meta2, col_meta3 = st.columns(3)
    with col_meta1:
        st.markdown(f"**📍 Campus Hub Location:** {college_record['location']}")
        st.markdown(f"**🏛️ Administrative Model:** {college_record['type']}")
    with col_meta2:
        st.markdown(f"**📜 NAAC Accreditation Grade:** {college_record['naac']}")
        st.markdown(f"**💼 Median Academic Placement:** {college_record['avg_package']} LPA")
    with col_meta3:
        st.markdown(f"**💰 Annual KEA Fee Matrix:** ₹{college_record['total_fee']:.2f} Lakhs/Year")
        st.markdown(f"**🏠 On-Campus Housing Availability:** {'Yes, Managed Internally' if college_record['hostel'] else 'No Housing Services'}")

    st.markdown(f"> **About Campus:** {college_record['about']}")
    st.markdown(f"🌐 **Official Institutional Link:** [{college_record['url']}]({college_record['url']})")

    st.markdown("---")
    st.subheader(f"📊 Multi-Year Cutoff Tracking & Predictions")

    branch_analysis_rows = []
    for branch_name, branch_data in college_record["branches"].items():
        raw_history = branch_data["history"]
        predicted_cutoff_2026 = get_predicted_2026_cutoff(college_record, user_category, branch_name)
        variance_delta = predicted_cutoff_2026 - user_rank
        
        if variance_delta > 15000:
            status_verdict = "Guaranteed Admission"
        elif variance_delta > 3000:
            status_verdict = "Highly Probable"
        elif variance_delta > 0:
            status_verdict = "Competitive Target"
        else:
            status_verdict = "Unlikely to Clear"

        quota_multiplier = {"GM": 1.0, "OBC": 1.35, "SC": 2.5, "ST": 2.8}.get(user_category, 1.0)
        
        branch_analysis_rows.append({
            "Engineering Stream": branch_name,
            "2021 Closing Cutoff": f"{round(raw_history[0] * quota_multiplier):,}",
            "2022 Closing Cutoff": f"{round(raw_history[1] * quota_multiplier):,}",
            "2023 Closing Cutoff": f"{round(raw_history[2] * quota_multiplier):,}",
            "2024 Closing Cutoff": f"{round(raw_history[3] * quota_multiplier):,}",
            "2025 Closing Cutoff": f"{round(raw_history[4] * quota_multiplier):,}",
            "Predicted 2026 Closing Cutoff": f"{predicted_cutoff_2026:,}",
            "Your Qualification Status": status_verdict
        })

    df_trends = pd.DataFrame(branch_analysis_rows)
    st.dataframe(df_trends, use_container_width=True, hide_index=True)

    # ── 12-COLUMN UNIFIED OVERALL STRATEGIC SCORECARD HUB TABLE FORMAT ──
    st.markdown("---")
    st.subheader(f"📋 Unified Institutional Metric Summary Table — {selected_college_name}")
    st.caption("Consolidating all analytical data parameters, packages, fees, predictions, and web endpoints into one master matrix.")

    agent_scorecard = run_all_agents(college_record, user_rank, user_category, user_location)
    
    meets_constraints = True
    if college_record["total_fee"] > user_budget: meets_constraints = False
    if user_hostel and not college_record["hostel"]: meets_constraints = False
    if user_location != "Any" and college_record["location"] != user_location: meets_constraints = False
    
    roi_label_val = str(agent_scorecard["roi"]["roi_label"]) if meets_constraints else "Excluded"

    master_scorecard_row = {
        "College Name": college_record["name"],
        "Location Hub": college_record["location"],
        "NAAC Rating": college_record["naac"],
        "Type (Model)": college_record["type"],
        "Annual Fee": f"₹{college_record['total_fee']:.2f}L",
        "Hostel Fee": f"₹{college_record['hostel_fee']:.2f}L" if college_record["hostel"] else "N/A",
        "Avg Package": f"{college_record['avg_package']} LPA",
        "Highest Package": f"{college_record['highest_package']} LPA",
        "Placed Companies": f"{len(college_record['companies'])} Top Recruiter Partners",
        "Official URL": college_record["url"],
        "Projected 2026 Cutoff (CSE)": f"{agent_scorecard['cutoff']['cutoff']:,}",
        "Chance of Admission (CSE)": agent_scorecard['cutoff']['chance_label']
    }

    df_master_scorecard = pd.DataFrame([master_scorecard_row])
    st.dataframe(df_master_scorecard, use_container_width=True, hide_index=True)
    
    st.markdown(" ")
    st.markdown("**Core Strategy Alignment Performance Summary:**")
    st.write(f"Composite Agent Pipeline Weighting Score: **{agent_scorecard['final_score']} / 10.0** | Financial Quota Return Class: **{roi_label_val}**")
