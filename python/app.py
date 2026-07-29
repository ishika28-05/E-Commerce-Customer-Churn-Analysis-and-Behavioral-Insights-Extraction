import streamlit as st
import pickle
import numpy as np
import pandas as pd
with open('python/churn_model.pkl','rb') as f:
    model = pickle.load(f)
with open('python/label_encoders.pkl','rb') as f:
    label_encoders = pickle.load(f)
st.set_page_config(page_title = "Customer Churn Predictor",page_icon = "🔴",layout = "centered")
st.title("🔴Customer Churn Predictor")
st.markdown("Enter customer details below to predict churn probability")
st.divider()
col1,col2,col3 = st.columns(3)
with col1:
    tenure = st.slider("Tenure(months)", 0,60,12)
    satisfaction = st.slider("Satisfaction Score", 1,5, 3)
    complain = st.selectbox("Filed a Complaint",["No","Yes"])
    city_tier = st.selectbox("City Tier", [1,2,3])
    warehouse_distance = st.slider("Warehouse to Home(km)",1,100,15)
    login_device = st.selectbox(options = label_encoders['PreferredLoginDevice'].classes_)
with col2:
    hour_on_app = st.slider("Hours on App",0,10,3)
    devices = st.slider("Number of Devices",1,6,3)
    order_count = st.slider("Order Count",1,30,5)
    cashback = st.slider("Cashback Amount",0,400,150)
    days_last_order = st.slider("Days Since Last Order",0,30,5)
    payment_mode = st.selectbox(options = label_encoders['PreferredPaymentMode'].classes_)
with col3:
    gender = st.selectbox(options = label_encoders['Gender'].classes_)
    order_category = st.selectbox(options = label_encoders['PreferedOrderCat'].classes_)
    marital_status = st.selectbox(options = label_encoders['MaritalStatus'].classes_)
    number_of_add = st.slider(options = label_encoders['NumberofAddress'].classes_)
    order_amt_hike_from_last_yr = st.slider(options = label_encoders['OrderAmountHikeFromlastYear'].classes_)
    coupon_used = st.slider(options = label_encoders['CouponUsed'].classes_)
st.divider()
if st.button("Predict Churn",type = "primary",use_container_width = True):
    login_device_val = label_encoders['PreferredLoginDevice'].transform([login_device])[0]
    payment_mode_val = label_encoders['PreferredPaymentMode'].transform([payment_mode])[0]
    gender_val = label_encoders['Gender'].transform([gender])[0]
    order_category_val = label_encoders['PreferedOrderCat'].transform([order_category])[0]
    marital_status_val = label_encoders['MaritalStatus'].transform([marital_status])[0]
    complain_val = 1 if complain == "Yes" else 0
    input_df = pd.DataFrame([{
    'Tenure': tenure,
    'PreferredLoginDevice': login_device_val,
    'CityTier': city_tier,
    'WarehouseToHome': warehouse_distance,
    'PreferredPaymentMode': payment_mode_val,
    'Gender': gender_val,
    'HourSpendOnApp': hour_on_app,
    'NumberOfDeviceRegistered': devices,
    'PreferedOrderCat': order_category_val,
    'SatisfactionScore': satisfaction,
    'MaritalStatus': marital_status_val,
    'NumberOfAddress': number_of_add,
    'Complain': complain_val,
    'OrderAmountHikeFromlastYear': order_amt_hike_from_last_yr,
    'CouponUsed': coupon_used,
    'OrderCount': order_count,
    'DaySinceLastOrder': days_last_order,
    'CashbackAmount': cashback
}])
    prob = model.predict_proba(input_df)[0][1]
    prediction = model.predict(input_df)[0]
    st.subheader("Prediction Result")
    if prediction == 1:
       st.error(f"⚠️ High Churn Risk -{prob*100:.1f}% probability of churning")
       st.markdown("**Recommended Action:** Send retention offer with increased cashback immediately")
    else:
       st.success(f"✅ Low Churn Risk -{prob*100:.1f}% probability of churning")
       st.markdown("**Recommended Action:** Continue standard engagement - customer is likely to stay")
    st.progress(prob)
    st.subheader("Key Factors Driving This Prediction")
    factors = {
       "Tenure" : f"{tenure} months - {'High Risk' if tenure < 6 else 'Low Risk'}",
       "Cashback" : f"{cashback} rupees - {'Above Average' if cashback > 150 else 'Below Average'}",
       "Complain" : f"{'Filed - Increases Risk' if complain=='Yes' else 'None - Reduces Risk'}",
       "Satisfaction" : f"{satisfaction}/5 - {'Low' if satisfaction<=2 else 'Acceptable' if satisfaction ==3 else 'Good'}"
        }
    for k,v in factors.items():
       st.markdown(f"- **{k}:** {v}")

    
    

                        
    
