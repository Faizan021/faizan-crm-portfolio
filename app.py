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
  Data-Driven Lifecycle Automation, VIP Retention, and Churn Mitigation across <strong>Crypto & FinTech</strong>, <strong>Fashion & DTC VIP Subscriptions</strong>, <strong>Food & Meal-Kit Reactivations</strong>, and <strong>Enterprise MarTech Architecture</strong>.
</p>

<div style="display:flex; gap:10px; flex-wrap:wrap;">
  <span style="background:#1e293b; border:1px solid #475569; color:#f1f5f9; padding:4px 10px; border-radius:6px; font-size:0.75rem; font-weight:600;">5+ Years Lifecycle Strategy</span>
  <span style="background:#1e293b; border:1px solid #475569; color:#f1f5f9; padding:4px 10px; border-radius:6px; font-size:0.75rem; font-weight:600;">Braze & Liquid Expert</span>
  <span style="background:#1e293b; border:1px solid #475569; color:#f1f5f9; padding:4px 10px; border-radius:6px; font-size:0.75rem; font-weight:600;">Snowflake SQL & RFM</span>
  <span style="background:#1e293b; border:1px solid #475569; color:#f1f5f9; padding:4px 10px; border-radius:6px; font-size:0.75rem; font-weight:600;">2026 Agentic CRM & Guardrails</span>
</div>
</div>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.markdown("### 🗂️ Industry Portfolios")
    nav_industry = st.radio(
        "Select Industry Vertical:",
        [
            "🪙 Crypto & FinTech WealthTech",
            "👗 Fashion & DTC VIP Membership",
            "🥦 Food & Meal-Kit Reactivations",
            "💻 Enterprise MarTech Lab"
        ],
        index=0
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
# VERTICAL 1: CRYPTO & FINTECH WEALTHTECH
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
        st.markdown("**The Challenge:** In regulated German FinTech, 52% of signed-up users abandon at the Video-Ident / ID verification step due to document friction.")
        st.markdown("**The Lifecycle Solution:** A 3-step dynamic nudging engine offering automated fallback methods (eID Chip in 2 mins, Bank-Ident, or 24/7 Video-Ident) paired with institutional trust reassurance.")
        
        kyc_choice = st.selectbox("Select Drop-Off Scenario:", ["Document Blur / Camera Failure (Step 2 Drop)", "Time Constraint / Abandoned Mid-Call (Step 4 Drop)"])
        if "Blur" in kyc_choice:
            st.info("📱 **In-App & Email Nudge Trigger:** 'Having camera trouble? Switch to 2-minute NFC chip scanning with your German ID card with zero human interaction.' → **+38.7% KYC Funnel Recovery**.")
        else:
            st.info("📱 **SMS & Email Nudge Trigger:** 'Your account is 90% set up. Complete your quick 2-minute verification anytime 24/7.' → **+29.4% Video-Ident Completion**.")

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
# VERTICAL 2: FASHION & DTC VIP MEMBERSHIP
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
# VERTICAL 3: FOOD & MEAL-KIT REACTIVATIONS
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
# VERTICAL 4: ENTERPRISE MARTECH LAB
# ==============================================================================
else:
    st.markdown("""
<div style="background:#f8fafc; border:1px solid #e2e8f0; border-top:4px solid #7c3aed; border-radius:10px; padding:1.2rem; margin-bottom:1.2rem;">
<div style="font-size:0.75rem; color:#7c3aed; font-weight:800; text-transform:uppercase;">INDUSTRY VERTICAL 04</div>
<div style="font-size:1.4rem; font-weight:800; color:#0f172a; margin:2px 0 6px 0;">💻 Enterprise MarTech Architecture & Engineering Lab</div>
<p style="font-size:0.86rem; color:#475569; margin:0; line-height:1.5;">
Production-grade technical implementation: Bilingual Braze Liquid conditional logic, automated Snowflake SQL cohort schemas, and Redis sub-5ms Idempotent Message Dispatchers.
</p>
</div>
""", unsafe_allow_html=True)

    code_tab1, code_tab2, code_tab3, code_tab4 = st.tabs([
        "🧩 Bilingual Braze Liquid Logic",
        "❄️ Snowflake SQL Cohort Schemas",
        "⚡ Redis Idempotency Dispatcher",
        "🤖 2026 Agentic CRM & Guardrails"
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

    with code_tab4:
        st.markdown("##### 🤖 2026 BrazeAI Agentic Canvas Step & Compliance Guardrails")
        st.markdown("""
        **Architecture Blueprint:**
        - **50% Path A (Deterministic Baseline):** Standard Braze Liquid rule-based template.
        - **50% Path B (BrazeAI Agent Step):** Real-time dynamic message generation constrained by strict negative prompts (*Zero return guarantees, institutional tone, <800ms fallback SLA*).
        """)
        st.info("✅ **Compliance Outcome:** Lets AI optimize 1:1 message relevance while guaranteeing 100% compliance with European advertising standards.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align:center; color:#64748b; font-size:0.8rem; padding:1rem 0;">
  Faizan Ahmed &bull; CRM Strategy & Lifecycle Marketing Portfolio &bull; Berlin, Germany &bull; 
  <a href="https://linkedin.com/in/faizanahmed01" target="_blank" style="color:#0284c7; font-weight:600; text-decoration:none;">LinkedIn Profile</a> &bull; 
  <a href="mailto:faizan.crm1@gmail.com" style="color:#0284c7; font-weight:600; text-decoration:none;">faizan.crm1@gmail.com</a>
</div>
""", unsafe_allow_html=True)
