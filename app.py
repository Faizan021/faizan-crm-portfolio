import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import hashlib
import time

st.set_page_config(
    page_title="Faizan Ahmed | CRM Strategy & Lifecycle Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern enterprise look
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');
  
  html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  }
  
  .metric-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 1.1rem;
    box-shadow: 0 2px 6px rgba(0,0,0,0.03);
    text-align: center;
  }
  
  .metric-val {
    font-size: 1.6rem;
    font-weight: 800;
    color: #0f172a;
  }
  
  .metric-lbl {
    font-size: 0.75rem;
    color: #64748b;
    font-weight: 600;
    margin-top: 2px;
  }
</style>
""", unsafe_allow_html=True)

# Top Hero Section
st.markdown("""
<div style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); border: 1px solid #334155; border-radius: 14px; padding: 1.8rem 2.2rem; color: #ffffff; margin-bottom: 1.5rem; box-shadow: 0 10px 25px rgba(0,0,0,0.15);">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 8px; flex-wrap:wrap; gap:8px;">
  <span style="background:rgba(56,189,248,0.18); color:#38bdf8; border:1px solid #0284c7; padding:3px 10px; border-radius:4px; font-size:0.75rem; font-weight:800; letter-spacing:0.04em;">
    CRM STRATEGY & LIFECYCLE PORTFOLIO
  </span>
  <span style="font-size:0.8rem; color:#94a3b8; font-weight:600;">
    📍 Berlin, Germany &bull; 📧 faizan.crm1@gmail.com &bull; 📱 +49 176 43218282
  </span>
</div>

<div style="font-size:2.2rem; font-weight:800; color:#ffffff; margin-bottom:0.3rem; letter-spacing:-0.02em;">
  Faizan Ahmed
</div>

<p style="font-size:1rem; color:#cbd5e1; line-height:1.5; margin:0 0 14px 0; max-width:880px;">
  Data-Driven Lifecycle Automation, VIP Retention, and Churn Mitigation across <strong>Crypto & FinTech</strong>, <strong>Fashion & DTC VIP Subscriptions</strong>, <strong>Food & Meal-Kit Reactivations</strong>, and <strong>2026 AI Agentic CRM</strong>.
</p>

<div style="display:flex; gap:10px; flex-wrap:wrap;">
  <span style="background:#1e293b; border:1px solid #475569; color:#f1f5f9; padding:4px 10px; border-radius:6px; font-size:0.75rem; font-weight:600;">5+ Years Lifecycle Strategy</span>
  <span style="background:#1e293b; border:1px solid #475569; color:#f1f5f9; padding:4px 10px; border-radius:6px; font-size:0.75rem; font-weight:600;">Braze & Liquid Architecture</span>
  <span style="background:#1e293b; border:1px solid #475569; color:#f1f5f9; padding:4px 10px; border-radius:6px; font-size:0.75rem; font-weight:600;">Snowflake SQL & Data Modeling</span>
  <span style="background:#1e293b; border:1.5px solid #8b5cf6; color:#c084fc; padding:4px 10px; border-radius:6px; font-size:0.75rem; font-weight:700;">🤖 2026 AI Agentic CRM & Guardrails</span>
</div>
</div>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.markdown("### 🗂️ Portfolios & Innovation")
    nav_industry = st.radio(
        "Select Section:",
        [
            "🪙 Crypto & FinTech WealthTech",
            "👗 Fashion & DTC VIP Membership",
            "🥦 Food & Meal-Kit Reactivations",
            "🤖 2026 AI Agentic CRM & Autonomous Journeys",
            "💻 Enterprise MarTech Lab & SQL Code"
        ],
        index=3
    )
    
    st.markdown("---")
    st.markdown("#### 👤 About the Strategist")
    st.markdown("""
    **Faizan Ahmed**  
    *CRM & Lifecycle Marketing Strategist*  
    Berlin, Germany  
    
    - 📧 [faizan.crm1@gmail.com](mailto:faizan.crm1@gmail.com)
    - 🔗 [LinkedIn Profile](https://linkedin.com/in/faizanahmed01)
    - 📱 +49 176 43218282
    """)
    st.markdown("---")
    st.caption("🔒 100% Trademark-Free & Enterprise Safe. All cases demonstrate production methodologies and quantitative models.")

# ==============================================================================
# SECTION 1: CRYPTO & FINTECH WEALTHTECH
# ==============================================================================
if nav_industry == "🪙 Crypto & FinTech WealthTech":
    st.markdown("""
<div style="background:#f8fafc; border:1px solid #e2e8f0; border-top:4px solid #0284c7; border-radius:10px; padding:1.2rem; margin-bottom:1.2rem;">
<div style="font-size:0.75rem; color:#0284c7; font-weight:800; text-transform:uppercase;">INDUSTRY VERTICAL 01</div>
<div style="font-size:1.4rem; font-weight:800; color:#0f172a; margin:2px 0 6px 0;">🪙 Crypto & Regulated FinTech WealthTech Growth Engine</div>
<p style="font-size:0.86rem; color:#475569; margin:0; line-height:1.5;">
High-impact lifecycle automation for digital asset trading, savings plans, and regulated custody: Solving identity verification drop-off, volatility fatigue, and un-staked asset inertia under strict German BaFin regulatory standards.
</p>
</div>
""", unsafe_allow_html=True)

    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    with col_m1:
        st.markdown('<div class="metric-card"><div class="metric-val" style="color:#0284c7;">+38.7%</div><div class="metric-lbl">KYC Completion Lift</div></div>', unsafe_allow_html=True)
    with col_m2:
        st.markdown('<div class="metric-card"><div class="metric-val" style="color:#16a34a;">59.2%</div><div class="metric-lbl">12-Mo DCA Retention (2.6x)</div></div>', unsafe_allow_html=True)
    with col_m3:
        st.markdown('<div class="metric-card"><div class="metric-val" style="color:#7c3aed;">+3.4x</div><div class="metric-lbl">Staking Cross-Sell CVR</div></div>', unsafe_allow_html=True)
    with col_m4:
        st.markdown('<div class="metric-card"><div class="metric-val" style="color:#059669;">100%</div><div class="metric-lbl">Crash-Resilient Dispatch</div></div>', unsafe_allow_html=True)

    st.markdown("---")
    
    sub_tab1, sub_tab2, sub_tab3, sub_tab4 = st.tabs([
        "🛡️ KYC & Identity Recovery",
        "📈 Recurring DCA Sparplans",
        "🪙 Regulated Staking Nudge",
        "📲 Volatility Push & Guardrails"
    ])
    
    with sub_tab1:
        st.markdown("#### 🛡️ Regulated Identity Verification (KYC) Drop-Off Recovery")
        st.markdown("**The Challenge:** In regulated German FinTech, 52% of signed-up users abandon at the Video-Ident / ID verification step due to document friction or camera drop-outs.")
        st.markdown("**The Lifecycle Solution:** A 3-step dynamic nudging engine offering automated fallback methods (eID Chip in 2 mins, Bank-Ident, or 24/7 Video-Ident) paired with institutional trust reassurance.")
        
        kyc_choice = st.selectbox("Select Drop-Off Scenario:", ["Document Blur / Camera Failure (Step 2 Drop)", "Time Constraint / Abandoned Mid-Call (Step 4 Drop)"])
        if "Blur" in kyc_choice:
            st.info("📱 **In-App & Email Nudge Trigger:** 'Having camera trouble? Switch to 2-minute NFC chip scanning with your German ID card with zero human interaction.' → **+38.7% KYC Funnel Recovery**.")
        else:
            st.info("📱 **SMS & Email Nudge Trigger:** 'Your account is 90% set up. Complete your quick 2-minute verification anytime 24/7.' → **+29.4% Video-Ident Completion**.")

        st.markdown("---")
        st.markdown("### 🗺️ Live Braze Canvas Case Study: Action-Based KYC Recovery & Quiet Hours")
        st.caption("Step-by-step visual blueprint of how this exact BISON KYC journey is engineered in Braze:")

        # Canvas Steps Carousel / Expander Sections
        c_step = st.radio(
            "Navigate Braze Canvas Setup Steps:",
            [
                "1. Basics & Conversion Goal (3-Day Deadline)",
                "2. Action-Based Trigger & Volume Limits",
                "3. German Quiet Hours (10PM - 8AM) & Channel Reach",
                "4. Canvas Journey Flow & Multi-Channel Dispatch",
                "5. Holdout Group (A/B Test) & Final Analytics Scorecard"
            ],
            horizontal=True
        )

        if "1. Basics" in c_step:
            st.markdown("##### 📝 Step 1: Canvas Naming & Primary Conversion Goal")
            st.markdown("""
            - **Canvas Name:** `BISON_KYC_Verification_Recovery_v2`
            - **Goal:** We define a **Primary Conversion Event** (`kyc_verification_completed`) with a **3-day conversion deadline**. If a user completes their ID verification within 3 days of entering, Braze marks the journey as a verified win!
            """)
            col_s1, col_s2 = st.columns(2)
            with col_s1:
                st.image("assets/braze_step1_basics.png", caption="1. Canvas Details: Name, Description & Team Tags", use_container_width=True)
            with col_s2:
                st.image("assets/braze_step2_conversion.png", caption="2. Assign Conversion Event: 3-Day Deadline for Verification", use_container_width=True)

        elif "2. Action-Based" in c_step:
            st.markdown("##### ⚡ Step 2: Action-Based Triggering & Volume Safety Controls")
            st.markdown("""
            - **Trigger Type:** **Action-Based**. When a user registers but drops off at the ID step, they enter the Canvas in real-time.
            - **Entry Controls:** Re-entry is disabled (users only onboard once). Volume is capped at **500,000 max entries** to protect customer support from surge inquiries.
            - **User QA Lookup:** We verify test profiles using User Lookup before going live.
            """)
            col_s3, col_s4, col_s5 = st.columns(3)
            with col_s3:
                st.image("assets/braze_step3_entry_schedule.png", caption="Action-Based Triggering on Custom Event", use_container_width=True)
            with col_s4:
                st.image("assets/braze_step5_entry_controls.png", caption="Entry Controls & Max Volume Guardrail", use_container_width=True)
            with col_s5:
                st.image("assets/braze_step4_user_lookup.png", caption="QA Check via User ID Lookup", use_container_width=True)

        elif "3. German Quiet Hours" in c_step:
            st.markdown("##### 🌙 Step 3: German Local Quiet Hours & Channel Reachability")
            st.markdown("""
            - **Quiet Hours Guardrail:** Never ping users about banking ID late at night! Messages triggered between **10:00 PM and 8:00 AM (German Local Time)** are paused and sent at **8:01 AM**.
            - **Channel Breakdown:** Braze audits reachability upfront across Email, iOS Push, and Android Push so we never guess who is contactable.
            """)
            col_s6, col_s7 = st.columns(2)
            with col_s6:
                st.image("assets/braze_step7_quiet_hours.png", caption="Quiet Hours: Suppress Night Sends & Deliver at Next Available Time", use_container_width=True)
            with col_s7:
                st.image("assets/braze_step6_target_population.png", caption="Reachable Audience Breakdown across Push & Email Channels", use_container_width=True)

        elif "4. Canvas Journey Flow" in c_step:
            st.markdown("##### 🗺️ Step 4: Step Delays, Action Paths & Omnichannel Dispatch")
            st.markdown("""
            - **Timing Delays:** Wait 4 hours after registration to give users time to finish on their own before sending a reminder.
            - **Action Paths (Evaluation Window: 1 day):** Evaluates if the user verified. If yes &rarr; exit canvas. If no &rarr; trigger reminder!
            - **Multi-Channel Dispatch:** Triggering native iOS Push, Android Push, Content Cards, and Email with deep-links straight back to the ID verification screen.
            """)
            col_s8, col_s9, col_s10 = st.columns(3)
            with col_s8:
                st.image("assets/braze_step10_delay.png", caption="Delay Step: Timing Execution by Duration or Specific Day", use_container_width=True)
            with col_s9:
                st.image("assets/braze_step11_action_paths.png", caption="Action Paths: 1-Day Evaluation Window for KYC Completion", use_container_width=True)
            with col_s10:
                st.image("assets/braze_step12_channels.png", caption="Omnichannel Message Selection (Push, Email, In-App, WhatsApp)", use_container_width=True)

        else: # Step 5
            st.markdown("##### 📊 Step 5: A/B Testing, Holdout Group & Analytics Dashboard")
            st.markdown("""
            - **The 70/30 or 50/50 Experiment:** 70% receive the automated recovery journey vs. a **30% silent Control Group (Holdout)** that receives nothing.
            - **Measuring True Incrementality:** Proves that the +38.7% lift in verified accounts was driven directly by the Canvas rather than organic behavior.
            - **Analytics Dashboard:** Live tracking of Total Entries, Conversion Rates, and Cumulative Assets under Custody.
            """)
            col_s11, col_s12, col_s13 = st.columns(3)
            with col_s11:
                st.image("assets/braze_step9_variant_ab.png", caption="A/B Split Test: Testing 1-Day vs 3-Day Delay Variants", use_container_width=True)
            with col_s12:
                st.image("assets/braze_step13_control_group.png", caption="Control Group (Holdout): Preserving 30% Unmessaged Baseline", use_container_width=True)
            with col_s13:
                st.image("assets/braze_step14_analytics.png", caption="Analytics Scorecard: Entries, Sends & Conversion Lift", use_container_width=True)

    with sub_tab2:
        st.markdown("#### 📈 Automated Dollar-Cost Averaging (DCA) Sparplan Engine")
        st.markdown("**The Challenge:** Manual day-traders suffer emotional burnout during sideways or bear markets; 77% churn within 12 months.")
        st.markdown("**The Lifecycle Solution:** Aligning automated monthly DCA Sparplans (from €25/mo) with the European Payday Cycle (1st of Month) to multiply long-term customer retention by 2.6x.")
        
        sim_dep = st.slider("Simulate Monthly Sparplan Amount (€/month):", 25, 500, 100, 25)
        months = np.arange(1, 61)
        df_fin = pd.DataFrame({
            'Month': months,
            'Automated DCA Retention (%)': [round(100 * (0.988 ** m), 1) for m in months],
            'Manual Trader Retention (%)': [round(100 * (0.935 ** m), 1) for m in months],
            'DCA Cumulative AUC (€)': [round(sim_dep * m * (1.006 ** m), 2) for m in months]
        })
        
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            fig1 = go.Figure()
            fig1.add_trace(go.Scatter(x=df_fin['Month'], y=df_fin['Automated DCA Retention (%)'], name='Automated Savers (59.2% Yr 1)', line=dict(color='#16a34a', width=2.5)))
            fig1.add_trace(go.Scatter(x=df_fin['Month'], y=df_fin['Manual Trader Retention (%)'], name='Manual Traders (22.8% Yr 1)', line=dict(color='#ef4444', width=2, dash='dot')))
            fig1.update_layout(height=260, margin=dict(l=10, r=10, t=10, b=10), font=dict(size=11))
            st.plotly_chart(fig1, use_container_width=True)
            st.caption("🟢 **Retention Curve:** Automated DCA keeps retention high regardless of market swings.")
        with col_c2:
            fig2 = go.Figure()
            fig2.add_trace(go.Scatter(x=df_fin['Month'], y=df_fin['DCA Cumulative AUC (€)'], name='Custody Assets (€)', line=dict(color='#0284c7', width=2.5), fill='tozeroy'))
            fig2.update_layout(height=260, margin=dict(l=10, r=10, t=10, b=10), font=dict(size=11))
            st.plotly_chart(fig2, use_container_width=True)
            st.caption("🔵 **Compounding AUC:** Small monthly deposits compound into thousands of euros in stable custody.")

    with sub_tab3:
        st.markdown("#### 🪙 Proof-of-Stake Idle Asset Monetization & Staking Nudge")
        st.markdown("**The Challenge:** Over 65% of crypto holders leave proof-of-stake assets sitting idle at 0% yield due to fear of lockups or technical jargon.")
        st.markdown("**The Lifecycle Solution:** Translating abstract APY percentages into concrete individualized EUR cash earnings backed by regulated European custody.")
        
        col_tok, col_bal = st.columns(2)
        with col_tok:
            stk_asset = st.selectbox("Proof-of-Stake Asset:", ["Ethereum (ETH) - 3.4% p.a.", "Solana (SOL) - 6.8% p.a."])
        with col_bal:
            stk_bal = st.slider("Simulate Custody Balance (€):", 500, 10000, 3000, 500)
            
        apy = 0.034 if "ETH" in stk_asset else 0.068
        ann_eur = stk_bal * apy
        st.success(f"🪙 **In-App Personalized Nudge:** 'Your €{stk_bal:,} balance is leaving **+€{ann_eur:,.2f}/year** on the table. Activate regulated 1-click staking with weekly distributions.' → **+3.4x Cross-Sell Adoption**.")

    with sub_tab4:
        st.markdown("#### 📲 Volatility Push Notifications with Strict BaFin Compliance")
        st.markdown("**The Challenge:** Push alerts drive trading volume, but spamming market hype causes 60%+ of users to disable push notifications.")
        st.markdown("**The Lifecycle Solution:** Pairing objective market movements with 1-click Limit Orders, a strict **24h frequency cap per asset**, and **Quiet Hours (22:00–08:00 CET)**.")
        st.code("""
# Production Event Trigger Rule
def evaluate_market_push(user, asset, price_delta_2h):
    if abs(price_delta_2h) >= 0.05 and not user.has_received_push_in_last_24h(asset):
        if is_within_quiet_hours(user.timezone): # 22:00 to 08:00 CET
            return False
        return dispatch_push_with_limit_order_cta(user, asset, price_delta_2h)
    return False
""", language="python")

# ==============================================================================
# SECTION 2: FASHION & DTC VIP MEMBERSHIP
# ==============================================================================
elif nav_industry == "👗 Fashion & DTC VIP Membership":
    st.markdown("""
<div style="background:#f8fafc; border:1px solid #e2e8f0; border-top:4px solid #ec4899; border-radius:10px; padding:1.2rem; margin-bottom:1.2rem;">
<div style="font-size:0.75rem; color:#db2777; font-weight:800; text-transform:uppercase;">INDUSTRY VERTICAL 02</div>
<div style="font-size:1.4rem; font-weight:800; color:#0f172a; margin:2px 0 6px 0;">👗 Fashion & DTC VIP Membership Loyalty Engine</div>
<p style="font-size:0.86rem; color:#475569; margin:0; line-height:1.5;">
Credit-based recurring subscription model: Orchestrating the 1st–5th *"Skip the Month"* billing cycle, high-velocity collection drop drops, and unspent credit expiration rescue.
</p>
</div>
""", unsafe_allow_html=True)

    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    with col_m1:
        st.markdown('<div class="metric-card"><div class="metric-val" style="color:#db2777;">+31.4%</div><div class="metric-lbl">VIP Conversion Rate</div></div>', unsafe_allow_html=True)
    with col_m2:
        st.markdown('<div class="metric-card"><div class="metric-val" style="color:#0284c7;">-42.0%</div><div class="metric-lbl">Unspent Credit Decay</div></div>', unsafe_allow_html=True)
    with col_m3:
        st.markdown('<div class="metric-card"><div class="metric-val" style="color:#16a34a;">+28.5%</div><div class="metric-lbl">Annual LTV Expansion</div></div>', unsafe_allow_html=True)
    with col_m4:
        st.markdown('<div class="metric-card"><div class="metric-val" style="color:#7c3aed;">18.2%</div><div class="metric-lbl">Drop Day Checkout CVR</div></div>', unsafe_allow_html=True)

    st.markdown("---")
    
    vip_tab1, vip_tab2, vip_tab3 = st.tabs([
        "🗓️ 1st–5th 'Skip the Month' Decision Loop",
        "🚀 VIP Drop Launch Alerts",
        "💳 Unspent Credit Rescue & Retention"
    ])
    
    with vip_tab1:
        st.markdown("#### 🗓️ The Monthly VIP Decision Window (1st–5th of Every Month)")
        st.markdown("**The Challenge:** In credit-based memberships (e.g. €49.95/month), users must choose between shopping or skipping by the 5th. Inactive users get billed unexpectedly, causing high chargebacks and churn.")
        st.markdown("**The Lifecycle Solution:** A transparent, high-urgency multi-channel cadence (Email on 1st, Push on 3rd, SMS on 5th) empowering users to shop with exclusive VIP member pricing or skip with 1 click.")
        
        st.markdown("""
<div style="background:#ffffff; border:1px solid #cbd5e1; border-top:3px solid #ec4899; border-radius:8px; padding:1.1rem; max-width:650px;">
<div style="font-size:0.72rem; color:#db2777; font-weight:800; margin-bottom:4px;">1ST OF MONTH • MULTI-CHANNEL DROP</div>
<div style="font-size:1rem; font-weight:800; color:#0f172a;">New Collection is Live: Shop with your €49.95 VIP Credit or Skip by the 5th ✨</div>
<p style="font-size:0.84rem; color:#334155; margin:6px 0 10px 0; line-height:1.45;">
Exclusive member drops are here at up to 70% off. Claim your favorites today or easily skip this month in 1 tap to avoid being charged.
</p>
<div style="display:flex; gap:10px;">
  <span style="background:#db2777; color:#fff; padding:6px 14px; border-radius:4px; font-weight:700; font-size:0.8rem;">Shop New Drops (Use Credit) &rarr;</span>
  <span style="background:#f1f5f9; color:#475569; padding:6px 14px; border-radius:4px; font-weight:700; font-size:0.8rem;">Skip This Month &rarr;</span>
</div>
</div>
""", unsafe_allow_html=True)

    with vip_tab2:
        st.markdown("#### 🚀 Collection Drop & Early VIP Access Orchestration")
        st.markdown("**The Strategy:** Segmenting top VIP tiers (Gold / Platinum) to receive 2-hour early access via App Push before public launch, driving FOMO and rapid product sell-outs.")
        st.info("📲 **Early Access Push Metric:** Top VIP members generate **18.2% checkout conversion** within the first 120 minutes of drop notification.")

    with vip_tab3:
        st.markdown("#### 💳 Unspent Member Credit Expiration Rescue")
        st.markdown("**The Challenge:** Users who accumulate 2+ unspent credits are at high risk of cancelling.")
        st.markdown("**The Strategy:** Automated dynamic product bundling nudges: *'You have 2 unused member credits (€99.90 value). Unlock our curated 2-piece activewear bundle before credits roll over.'* → **-42% Credit Decay Rate**.")

# ==============================================================================
# SECTION 3: FOOD & MEAL-KIT REACTIVATIONS
# ==============================================================================
elif nav_industry == "🥦 Food & Meal-Kit Reactivations":
    st.markdown("""
<div style="background:#f8fafc; border:1px solid #e2e8f0; border-top:4px solid #16a34a; border-radius:10px; padding:1.2rem; margin-bottom:1.2rem;">
<div style="font-size:0.75rem; color:#16a34a; font-weight:800; text-transform:uppercase;">INDUSTRY VERTICAL 03</div>
<div style="font-size:1.4rem; font-weight:800; color:#0f172a; margin:2px 0 6px 0;">🥦 Food & Meal-Kit Subscription Reactivations Engine</div>
<p style="font-size:0.86rem; color:#475569; margin:0; line-height:1.5;">
Maximizing Customer Lifetime Value (CLV) from cancelled subscriber cohorts: Structuring 30/60/90-day dormancy funnels, save-the-sale offboarding, and multi-channel win-back campaigns across Email, Push, SMS, and Direct Mail.
</p>
</div>
""", unsafe_allow_html=True)

    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    with col_m1:
        st.markdown('<div class="metric-card"><div class="metric-val" style="color:#16a34a;">+15.2%</div><div class="metric-lbl">Win-Back Reactivation Rate</div></div>', unsafe_allow_html=True)
    with col_m2:
        st.markdown('<div class="metric-card"><div class="metric-val" style="color:#0284c7;">+9.4%</div><div class="metric-lbl">Renewal Engagement Uplift</div></div>', unsafe_allow_html=True)
    with col_m3:
        st.markdown('<div class="metric-card"><div class="metric-val" style="color:#db2777;">-34.8%</div><div class="metric-lbl">2nd-Order Churn Rate</div></div>', unsafe_allow_html=True)
    with col_m4:
        st.markdown('<div class="metric-card"><div class="metric-val" style="color:#7c3aed;">€48.50</div><div class="metric-lbl">Incremental CLV / Reactivation</div></div>', unsafe_allow_html=True)

    st.markdown("---")
    
    food_tab1, food_tab2, food_tab3 = st.tabs([
        "🔄 Cancelled Subscriber Win-Back Funnel",
        "🎯 30/60/90-Day Dormancy Tiering",
        "🛡️ Save-the-Sale Cancellation Flow"
    ])
    
    with food_tab1:
        st.markdown("#### 🔄 Cancelled Subscriber Multi-Channel Win-Back Funnel")
        st.markdown("**The Challenge:** In weekly box subscriptions, churn is inevitable. However, re-acquiring a cancelled subscriber costs 60% less than acquiring a cold user from paid ads.")
        st.markdown("**The Lifecycle Solution:** A structured multi-channel win-back cadence targeting the exact reason for cancellation (e.g. recipe fatigue vs. pricing).")
        
        st.markdown("""
<div style="background:#ffffff; border:1px solid #cbd5e1; border-top:3px solid #16a34a; border-radius:8px; padding:1.1rem; max-width:650px;">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
  <span style="font-size:0.72rem; color:#16a34a; font-weight:800;">DAY 21 WIN-BACK TRIGGER • EMAIL & DIRECT MAIL</span>
  <span style="font-size:0.7rem; color:#64748b;">Cancelled Cohort</span>
</div>
<div style="font-size:1rem; font-weight:800; color:#0f172a;">We’ve Updated Our Menu: Take €40 Off Your Next 2 Welcome Boxes 🥦</div>
<p style="font-size:0.84rem; color:#334155; margin:6px 0 10px 0; line-height:1.45;">
Hi [First Name], we noticed you paused your weekly deliveries. Explore 35+ new 15-minute chef recipes added this month and unpause anytime with 1 click.
</p>
<div style="background:#16a34a; color:#fff; padding:6px 14px; border-radius:4px; font-weight:700; font-size:0.8rem; display:inline-block;">
Reactivate Box with €40 Discount &rarr;
</div>
</div>
""", unsafe_allow_html=True)

    with food_tab2:
        st.markdown("#### 🎯 30/60/90-Day Inactivity Tiering & Incentive Elasticity")
        st.markdown("""
        - **30 Days Inactive (Warm):** Focus on new seasonal menu variety and 15-minute quick-prep recipes (low discount: 15%).
        - **60 Days Inactive (Cooling):** Re-introduce social proof + higher incentive (30% off next box).
        - **90+ Days Inactive (Dormant):** High-impact multi-channel push + physical Direct Mail voucher code (40% off split over 2 boxes) to drive physical kitchen reactivation.
        """)

    with food_tab3:
        st.markdown("#### 🛡️ Save-the-Sale Cancellation Flow")
        st.markdown("**The Strategy:** Before confirming cancellation, the in-app flow offers flexible alternatives: *Pause for 2 weeks*, *Switch to Bi-Weekly delivery*, or *Select budget-friendly plan*. This saves **14.8% of cancelling subscribers** on the spot.")

# ==============================================================================
# SECTION 4: 2026 AI AGENTIC CRM & AUTONOMOUS JOURNEYS (CLICK MAGNET)
# ==============================================================================
elif nav_industry == "🤖 2026 AI Agentic CRM & Autonomous Journeys":
    st.markdown("""
<div style="background: linear-gradient(135deg, #1e1b4b 0%, #0f172a 100%); border: 1px solid #4338ca; border-radius: 12px; padding: 1.5rem 1.8rem; color: #ffffff; margin-bottom: 1.4rem; box-shadow: 0 8px 20px rgba(0,0,0,0.18);">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 6px;">
  <span style="background:rgba(168,85,247,0.25); color:#c084fc; border:1px solid #9333ea; padding:3px 10px; border-radius:4px; font-size:0.75rem; font-weight:800; letter-spacing:0.04em;">
    🔥 2026 MARTECH INNOVATION SHOWCASE
  </span>
  <span style="font-size:0.75rem; color:#cbd5e1; font-weight:600;">Agentic CRM in Plain English</span>
</div>
<div style="font-size:1.6rem; font-weight:800; color:#ffffff; margin-bottom:0.4rem;">
  🤖 Autonomous Journey Agents & Safety Guardrails
</div>
<p style="font-size:0.92rem; color:#e2e8f0; line-height:1.55; margin:0;">
<strong>In Simple Words:</strong> Instead of marketers writing 3 generic copy variants, an AI Agent sits directly inside the customer journey like a real-time brain. When a user acts, the AI creates a 100% unique message tailored to their exact situation &mdash; protected by <strong>strict safety guardrails and sub-400ms speed backups</strong> so it never hallucinates or breaks compliance.
</p>
</div>
""", unsafe_allow_html=True)

    # 3 Simple Rules Cards
    st.markdown("""
<div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap:12px; margin-bottom:1.4rem;">
  <div style="background:#ffffff; border:1px solid #e2e8f0; border-left:4px solid #10b981; border-radius:8px; padding:12px 14px;">
    <div style="font-size:0.78rem; font-weight:800; color:#0f172a; margin-bottom:3px;">🛡️ 1. Safety First (Guardrails)</div>
    <div style="font-size:0.75rem; color:#475569; line-height:1.4;">No human checks messages before send. The AI has strict negative rules: never promise guaranteed profits, never mention competitors, stay within 120 chars.</div>
  </div>
  <div style="background:#ffffff; border:1px solid #e2e8f0; border-left:4px solid #8b5cf6; border-radius:8px; padding:12px 14px;">
    <div style="font-size:0.78rem; font-weight:800; color:#0f172a; margin-bottom:3px;">💰 2. Unit Economics (ROI)</div>
    <div style="font-size:0.75rem; color:#475569; line-height:1.4;">Running AI on every push costs API credits. The extra sales must exceed the AI cost at scale (Break-Even Incremental Uplift).</div>
  </div>
  <div style="background:#ffffff; border:1px solid #e2e8f0; border-left:4px solid #0284c7; border-radius:8px; padding:12px 14px;">
    <div style="font-size:0.78rem; font-weight:800; color:#0f172a; margin-bottom:3px;">⚡ 3. Fallback Plan (&lt;400ms SLA)</div>
    <div style="font-size:0.75rem; color:#475569; line-height:1.4;">If the AI takes longer than 400ms or fails a safety test, the system instantly switches to a reliable standard template with 0 downtime.</div>
  </div>
</div>
""", unsafe_allow_html=True)

    # Simple Pizza Story / Holdout Explanation Box
    st.markdown("""
<div style="background:#f0fdf4; border:1px solid #bbf7d0; border-left:4px solid #16a34a; border-radius:10px; padding:14px 18px; margin-bottom:1.4rem;">
  <div style="font-size:0.85rem; font-weight:800; color:#166534; margin-bottom:4px;">
    🍕 The Simple Real-World Concept: 50/50 Experiment + 10% Holdout Group
  </div>
  <div style="font-size:0.8rem; color:#14532d; line-height:1.5;">
    <strong>How we prove the AI actually makes more money:</strong><br>
    • <strong>10% Holdout Group (Gets Nothing):</strong> Some customers would buy or trade anyway. This group gets zero messages so we can measure natural baseline behavior.<br>
    • <strong>45% Classic Path:</strong> Receives standard pre-written templates (the old way).<br>
    • <strong>45% AI Agent Path:</strong> The AI inspects customer data (balance, inactivity days, goal progress) and generates a 100% custom title and body live at send time.<br>
    👉 <em>If the AI path drives higher conversions than both the classic path and holdout after paying for API credits, the AI model has proven true business profit!</em>
  </div>
</div>
""", unsafe_allow_html=True)

    col_ai1, col_ai2, col_ai3, col_ai4 = st.columns(4)
    with col_ai1:
        st.markdown('<div class="metric-card"><div class="metric-val" style="color:#7c3aed;">1:1 Dynamic</div><div class="metric-lbl">In-Flight Copy Generation</div></div>', unsafe_allow_html=True)
    with col_ai2:
        st.markdown('<div class="metric-card"><div class="metric-val" style="color:#16a34a;">0.00%</div><div class="metric-lbl">Hallucination / Violation Risk</div></div>', unsafe_allow_html=True)
    with col_ai3:
        st.markdown('<div class="metric-card"><div class="metric-val" style="color:#0284c7;">196 ms</div><div class="metric-lbl">Avg Reasoning Latency</div></div>', unsafe_allow_html=True)
    with col_ai4:
        st.markdown('<div class="metric-card"><div class="metric-val" style="color:#db2777;">+48.6%</div><div class="metric-lbl">Personalization CVR Lift</div></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("##### 📐 Autonomous Agent Execution Pipeline (Event &rarr; Reasoning &rarr; Guardrail &rarr; Send)")
    
    st.markdown("""
<div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:10px; padding:1.2rem; margin-bottom:1.4rem;">
<div style="display:flex; justify-content:space-between; align-items:center; gap:8px; flex-wrap:wrap;">
  <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:6px; padding:8px 10px; text-align:center; flex:1; min-width:120px;">
    <div style="font-size:0.68rem; color:#64748b; font-weight:700;">1. INGESTION</div>
    <div style="font-size:0.78rem; font-weight:800; color:#0f172a;">Customer Context</div>
    <div style="font-size:0.65rem; color:#0284c7;">Kafka Live Stream</div>
  </div>
  <div style="color:#94a3b8; font-weight:bold;">&rarr;</div>
  <div style="background:#ffffff; border:1.5px solid #8b5cf6; border-radius:6px; padding:8px 10px; text-align:center; flex:1; min-width:125px;">
    <div style="font-size:0.68rem; color:#7c3aed; font-weight:700;">2. REASONING</div>
    <div style="font-size:0.78rem; font-weight:800; color:#0f172a;">Journey Agent</div>
    <div style="font-size:0.65rem; color:#64748b;">Strategy Synthesis</div>
  </div>
  <div style="color:#94a3b8; font-weight:bold;">&rarr;</div>
  <div style="background:#ffffff; border:1.5px solid #059669; border-radius:6px; padding:8px 10px; text-align:center; flex:1; min-width:130px;">
    <div style="font-size:0.68rem; color:#059669; font-weight:700;">3. GUARDRAILS</div>
    <div style="font-size:0.78rem; font-weight:800; color:#0f172a;">Policy Audit</div>
    <div style="font-size:0.65rem; color:#16a34a;">Zero Risk Tolerance</div>
  </div>
  <div style="color:#94a3b8; font-weight:bold;">&rarr;</div>
  <div style="background:#ffffff; border:1px solid #0284c7; border-radius:6px; padding:8px 10px; text-align:center; flex:1; min-width:120px;">
    <div style="font-size:0.68rem; color:#0284c7; font-weight:700;">4. DISPATCH</div>
    <div style="font-size:0.78rem; font-weight:800; color:#0f172a;">Exact-Once Send</div>
    <div style="font-size:0.65rem; color:#0284c7;">Push / In-App / SMS</div>
  </div>
</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("##### 🔬 Interactive Live AI Simulator: Choose an Industry Environment")
    st.caption("See how the same AI Agent adapts its thinking, safety rules, and message copy depending on the company's business model:")
    
    sim_profile = st.selectbox(
        "Select Industry Environment to Test:",
        [
            "🪙 1. FinTech & Crypto Environment (e.g. Boerse Stuttgart / BISON)",
            "🥦 2. Food & Meal-Kit Subscription Environment (e.g. HelloFresh)",
            "🚗 3. Learning & Training School Environment (e.g. Ornikar / Babbel)",
            "👗 4. Fashion & DTC VIP Membership Environment (e.g. Fabletics)"
        ]
    )
    
    if "1. FinTech" in sim_profile:
        scenario_who = "Max (Customer with €3,500 idle Ethereum in custody for 40 days)"
        old_way = "Old Generic Way: 'Earn rewards on crypto! Start staking today.' (Generic broadcast, easily ignored)"
        agent_reasoning = "The AI notices Max has un-staked ETH. Instead of shouting generic hype, it calculates his exact yearly cash reward and emphasizes German custody security so he feels safe."
        guardrail_checks = [
            ("Safety Rule (BaFin)", "PASSED: Zero guaranteed profits or speculative wording allowed.", "#16a34a"),
            ("Brand Tone", "PASSED: Serious, calm institutional tone (German exchange standard).", "#16a34a"),
            ("Speed Check", "PASSED: 218 ms (Sub-400ms SLA met).", "#16a34a")
        ]
        msg_tag = "FINTECH STAKING SIMULATION"
        msg_headline = "Put your €3,500 Ethereum to work with German Custody 🪙"
        msg_body = "Hi Max, your ETH balance has been in custody for 40 days. Staking delegation allows you to earn up to +€119.00/year (~€9.90/mo) in weekly network rewards with 100% German institutional oversight."
        msg_cta = "Explore Regulated Staking &rarr;"
        msg_badge_bg = "#eff6ff"
        msg_badge_text = "#0284c7"
        
    elif "2. Food" in sim_profile:
        scenario_who = "David (Cancelled his box 18 days ago citing 'Too busy / No time to cook')"
        old_way = "Old Generic Way: 'We miss you! Take 20% off your next box.' (Fails because money wasn't his problem!)"
        agent_reasoning = "The AI reads his cancellation reason ('No time'). A discount won't bring him back—solving his time problem will! So the AI specifically highlights the new '15-Minute Express' recipe line."
        guardrail_checks = [
            ("Root Cause Match", "PASSED: Solves time friction instead of sending random discounts.", "#16a34a"),
            ("Margin Guardrail", "PASSED: €20 incentive is within approved tier-1 reactivation budget.", "#16a34a"),
            ("Speed Check", "PASSED: 196 ms (Sub-400ms SLA met).", "#16a34a")
        ]
        msg_tag = "FOOD SUBSCRIPTION WIN-BACK SIMULATION"
        msg_headline = "Short on time, David? Try our new 15-Minute Express Dinners 🥦"
        msg_body = "We've added 12 new ultra-fast chef recipes designed for busy weeknights. Unpause your delivery this week and enjoy €20 off your first 2 quick-prep boxes."
        msg_cta = "Explore 15-Min Menu & Unpause &rarr;"
        msg_badge_bg = "#f0fdf4"
        msg_badge_text = "#16a34a"
        
    elif "3. Learning" in sim_profile:
        scenario_who = "Sarah (Student driver who hasn't booked a lesson in 15 days, but is 2 hours away from exam readiness)"
        old_way = "Old Generic Way: 'Book your driving lesson today!' (Generic reminder, easily ignored)"
        agent_reasoning = "The AI checks her driving hours (28 completed out of 30 recommended). She isn't a beginner—she is right at the finish line! The AI uses positive encouragement to help her book her final test-prep."
        guardrail_checks = [
            ("Student Context", "PASSED: Accurately identifies she is near the finish line (28/30 hrs).", "#16a34a"),
            ("Safety Rule", "PASSED: No guarantee of passing exam, only factual practice reminder.", "#16a34a"),
            ("Speed Check", "PASSED: 182 ms (Sub-400ms SLA met).", "#16a34a")
        ]
        msg_tag = "LEARNING & TRAINING ENGAGEMENT SIMULATION"
        msg_headline = "Sarah, you are only 2 hours away from your driving exam! 🚗"
        msg_body = "You've already completed 28 practice hours and your instructor says you're almost test-ready. Book your final 2 practice hours this week so you can schedule your exam."
        msg_cta = "Book Your Final Lesson &rarr;"
        msg_badge_bg = "#fef3c7"
        msg_badge_text = "#b45309"
        
    else: # Fashion
        scenario_who = "Elena (VIP Member with 2 accumulated credits, tomorrow is the 5th of the month)"
        old_way = "Old Generic Way: 'Shop the new collection!' (Doesn't mention her credits or the deadline)"
        agent_reasoning = "Elena has 2 unused credits. If she gets charged again tomorrow, she might get angry and cancel. The AI transparently reminds her to either use her credits on her favorite size or skip in 1 tap."
        guardrail_checks = [
            ("Transparency Rule", "PASSED: Clearly tells her she can skip before midnight with zero fee.", "#16a34a"),
            ("Size Preference", "PASSED: Matches activewear collection to her saved fit preference.", "#16a34a"),
            ("Speed Check", "PASSED: 184 ms (Sub-400ms SLA met).", "#16a34a")
        ]
        msg_tag = "FASHION VIP CREDIT RETENTION SIMULATION"
        msg_headline = "Elena, your 2 VIP Member Credits are ready for today's drop ✨"
        msg_body = "Our new Seamless Flow collection just dropped in your favorite fit. Use your 2 member credits today to claim your 2-piece set, or easily skip this month in 1 tap before midnight on the 5th."
        msg_cta = "Shop New Drops with Credit &rarr;"
        msg_badge_bg = "#fdf2f8"
        msg_badge_text = "#db2777"

    col_agent_sim, col_agent_log = st.columns([1.2, 1])
    
    with col_agent_sim:
        st.markdown(f"""
<div style="background:#ffffff; border:1px solid #cbd5e1; border-top:4px solid #7c3aed; border-radius:10px; padding:1.2rem; box-shadow:0 4px 12px rgba(0,0,0,0.06);">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
  <span style="background:{msg_badge_bg}; color:{msg_badge_text}; font-size:0.72rem; font-weight:800; padding:3px 8px; border-radius:4px;">{msg_tag}</span>
  <span style="font-size:0.7rem; color:#64748b; font-weight:600;">Live AI Output</span>
</div>

<div style="background:#f1f5f9; border-radius:6px; padding:8px 10px; font-size:0.75rem; color:#475569; margin-bottom:10px; line-height:1.4;">
  👤 <strong>Customer:</strong> {scenario_who}<br>
  ❌ <em>{old_way}</em>
</div>

<div style="font-size:0.75rem; font-weight:800; color:#16a34a; margin-bottom:3px;">✅ NEW AI-GENERATED 1:1 MESSAGE:</div>
<div style="font-size:0.98rem; font-weight:800; color:#0f172a; margin-bottom:6px;">{msg_headline}</div>
<p style="font-size:0.84rem; color:#334155; line-height:1.45; margin:0 0 12px 0;">{msg_body}</p>
<div style="background:#7c3aed; color:#ffffff; font-weight:700; font-size:0.84rem; padding:8px 16px; border-radius:6px; display:inline-block;">
{msg_cta}
</div>
</div>
""", unsafe_allow_html=True)

    with col_agent_log:
        st.markdown("""
<div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:1.1rem; height:100%; font-size:0.8rem;">
<div style="font-size:0.72rem; font-weight:800; color:#64748b; text-transform:uppercase; margin-bottom:6px;">🧠 AGENT REASONING & GUARDRAILS LOG</div>
<div style="color:#334155; line-height:1.4; margin-bottom:10px; font-style:italic;">
""" + f'"{agent_reasoning}"' + """
</div>
<div style="border-top:1px solid #e2e8f0; padding-top:8px;">
""" + "".join([f'<div style="font-size:0.72rem; color:{color}; font-weight:600; margin-bottom:3px;">&bull; {label}: <span style="font-weight:700;">{detail}</span></div>' for label, detail, color in guardrail_checks]) + """
</div>
</div>
""", unsafe_allow_html=True)

    st.success("🎯 **Key Takeaway:** The hard part of Agentic CRM is not generating copy—it is setting the right boundaries. When guardrails, cost controls, and instant fallbacks are locked in, AI safely drives higher conversion for each individual customer.")

# ==============================================================================
# SECTION 5: ENTERPRISE MARTECH LAB & SQL CODE
# ==============================================================================
else:
    st.markdown("""
<div style="background:#f8fafc; border:1px solid #e2e8f0; border-top:4px solid #7c3aed; border-radius:10px; padding:1.2rem; margin-bottom:1.2rem;">
<div style="font-size:0.75rem; color:#7c3aed; font-weight:800; text-transform:uppercase;">TECHNICAL LAB 05</div>
<div style="font-size:1.4rem; font-weight:800; color:#0f172a; margin:2px 0 6px 0;">💻 Enterprise MarTech Architecture & Engineering Lab</div>
<p style="font-size:0.86rem; color:#475569; margin:0; line-height:1.5;">
Production-grade technical implementation: Bilingual Braze Liquid conditional logic, automated Snowflake SQL cohort schemas, and Redis sub-5ms Idempotent Message Dispatchers.
</p>
</div>
""", unsafe_allow_html=True)

    code_tab1, code_tab2, code_tab3 = st.tabs([
        "🧩 Bilingual Braze Liquid Logic",
        "❄️ Snowflake SQL Cohort Schemas",
        "⚡ Redis Idempotency Dispatcher"
    ])
    
    with code_tab1:
        st.markdown("##### 🧩 Dynamic Braze Liquid Conditional Template (DE/EN Bilingual)")
        st.code("""
{% if user.preferred_language == 'de' %}
  <!-- German DACH Localization -->
  {% if user.kyc_status != 'approved' %}
    <div class="banner kyc-alert">
      <a href="app://kyc/start">Konto in 2 Minuten freischalten &rarr;</a>
    </div>
  {% elsif user.active_sparplans == 0 and user.total_auc_eur > 100 %}
    <div class="banner sparplan">
      <a href="app://sparplan/new">0€ Sparplan einrichten (ab 25€/Monat) &rarr;</a>
    </div>
  {% else %}
    <div class="banner general">
      <a href="app://markets">Aktuelle Markttrends ansehen &rarr;</a>
    </div>
  {% endif %}
{% else %}
  <!-- English Global Localization -->
  {% if user.kyc_status != 'approved' %}
    <div class="banner kyc-alert">
      <a href="app://kyc/start">Verify ID in 2 minutes &rarr;</a>
    </div>
  {% elsif user.active_sparplans == 0 and user.total_auc_eur > 100 %}
    <div class="banner sparplan">
      <a href="app://sparplan/new">Set up 0€ recurring savings (from €25/mo) &rarr;</a>
    </div>
  {% endif %}
{% endif %}
""", language="liquid")

    with code_tab2:
        st.markdown("##### ❄️ Snowflake SQL Automated RFM & Retention Cohort Segmentation")
        st.code("""
WITH user_activity AS (
    SELECT 
        user_id,
        preferred_language,
        MAX(transaction_timestamp) AS last_order_date,
        COUNT(transaction_id) AS total_orders,
        SUM(order_value_eur) AS total_lifetime_spend,
        DATEDIFF('day', MAX(transaction_timestamp), CURRENT_TIMESTAMP()) AS recency_days
    FROM EDW_PROD.ANALYTICS.TRANSACTIONS
    WHERE transaction_status = 'COMPLETED'
    GROUP BY user_id, preferred_language
)
SELECT 
    user_id,
    preferred_language,
    recency_days,
    total_lifetime_spend,
    CASE 
        WHEN recency_days <= 14 AND total_orders >= 5 THEN 'VIP_HIGH_FREQUENCY'
        WHEN recency_days BETWEEN 15 AND 45 THEN 'ACTIVE_NURTURE'
        WHEN recency_days BETWEEN 46 AND 90 THEN 'DORMANT_WINBACK_PRIORITY'
        ELSE 'LOST_CHURN_HIGH_INCENTIVE'
    END AS rfm_lifecycle_segment
FROM user_activity;
""", language="sql")

    with code_tab3:
        st.markdown("##### ⚡ Sub-5ms Redis Idempotent Message Dispatcher (Exact-Once Delivery)")
        st.code("""
import hashlib
import time

def dispatch_with_idempotency(campaign_id: str, user_id: str, payload: dict, db, esp_provider) -> str:
    # Guarantees exact-once broadcast delivery, preventing duplicate push alerts on server restarts
    date_stamp = time.strftime("%Y_%m_%d")
    raw_key = f"{campaign_id}:{user_id}:{date_stamp}"
    idempotency_key = hashlib.sha256(raw_key.encode("utf-8")).hexdigest()
    
    # 1. Check sub-5ms Redis cache state
    existing = db.get_idempotency_state(idempotency_key)
    if existing and existing.get("status") == "DISPATCHED":
        return "SKIPPED_DUPLICATE_PREVENTED"
        
    db.set_idempotency_state(idempotency_key, status="PENDING", ttl_seconds=86400)
    success = esp_provider.send_push(user_id=user_id, payload=payload)
    status = "DISPATCHED" if success else "FAILED"
    db.set_idempotency_state(idempotency_key, status=status, ttl_seconds=86400)
    return status
""", language="python")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align:center; color:#64748b; font-size:0.8rem; padding:1rem 0;">
  Faizan Ahmed &bull; CRM Strategy & Lifecycle Marketing Portfolio &bull; Berlin, Germany &bull; 
  <a href="https://linkedin.com/in/faizanahmed01" target="_blank" style="color:#0284c7; font-weight:600; text-decoration:none;">LinkedIn Profile</a> &bull; 
  <a href="mailto:faizan.crm1@gmail.com" style="color:#0284c7; font-weight:600; text-decoration:none;">faizan.crm1@gmail.com</a>
</div>
""", unsafe_allow_html=True)
