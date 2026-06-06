import streamlit as st
import joblib


captains = {
    "Argentina": {
        "name": "Lionel Messi",
        "role": "Captain",
        "image": "https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcTa5lV61pLYakS2L5pkWo8-UlCxor7mIXtg1lecK7-rD3F4tmD9mATpzVJZxab0fOQlTLxKZ3_uR05kKpo"
    },

    "Brazil": {
        "name": "Marquinhos",
        "role": "Captain",
        "image": "https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcTM2cw_2Gra8ai-jhnHt4RI0vO-wrDWVLUWsDPopekMd2t8kFny7V_kkRDJoe4CoSMVCtxGZmpmz_zbRGM"
    },

    "France": {
        "name": "Kylian Mbappe",
        "role": "Captain",
        "image": "https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcQQpYr4_EGaLn_-yuvoaPbaPqfhHzh5X4fyeOu-P6VL1N3QYqeVWx5yhhFuDfIUsfXcuCl7AVCl_DMDlsA"
    },

    "England": {
        "name": "Harry Kane",
        "role": "Captain",
        "image": "https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcSCBtqxRclcXALZOiGRSEF6R3PKr-Scv669SPnxNYusluy31iUB3vM7dYAA_B7mXduazi81c-G1ewee_zA"
    },

    "Spain": {
        "name": "Alvaro Morata",
        "role": "Captain",
        "image": "https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcQ2c727btx2hlSz8Yb7gdiQKtrpNIqeDIQZfBDK6wBuhpmk9XzENDfPdCDhIFsHSYSUQy6P8ZkEcdS3iVw"
    },

    "Portugal": {
        "name": "Cristiano Ronaldo",
        "role": "Captain",
        "image": "https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcSt5O1BPWiDhy0Ue80X0pBXss6hD298AAyy2WHzk90vK_EBKXTpcmJuONYQ_fkYHSQv9Sw2a8iUFLcLr-4"
    }
}
# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="FIFA World Cup Predictor",
    page_icon="🏆",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp {
    background-image: url("https://images.openai.com/static-rsc-4/hi8sz8KqcWf_Q0aoNfxC0ZyfbG4zv0PEmkIc3Z0KYNNraLy86JM6Ii77_snQPJPuRAZHaM9vEwv4VXsRpFM8IKYOoqN5P0MdWFVi_DFi1b40BK6WJpoIl2fP7FMB2Cd4-z8OSbLUydOn0L6WLiF3mNCLpIpesbpkL4PvKLObbvmcSm_4wxJmUH_WnDL8Z_Jj?purpose=fullsize");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

.main-card {
    background-color: rgba(0,0,0,0.75);
    padding: 25px;
    border-radius: 15px;
}

h1, h2, h3 {
    text-align: center;
}

.result-box {
    background-color: rgba(255,215,0,0.15);
    border: 2px solid gold;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 28px;
    font-weight: bold;
}
            
.captain-card {
    background-color: rgba(255,255,255,0.1);
    padding: 15px;
    border-radius: 15px;
    text-align: center;
    margin-top: 10px;
}
            
.captain-img {
    width: 200px;           /* Forces identical width across all images */
    height: 270px;          /* Forces identical height across all images */
    object-fit: cover;      /* Crops the image to fit the container without distortion */
    object-position: top center; /* Focuses the crop on the player's face/head area */
    border-radius: 12px;    /* Matches the clean rounded corners in your screenshot */
}
            
/* ... keep your existing styles ... */

/* This targets the images inside your columns/cards specifically */
[data-testid="stImage"] img {
    width: 200px !important;
    height: 270px !important;
    object-fit: cover !important;
    object-position: top center !important;
    border-radius: 12px !important;
}

/* Optional: Center the image wrapper if it's in a column */
[data-testid="stImage"] {
    display: flex;
    justify-content: center;
}


</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
model = joblib.load("model/model.pkl")

home_encoder = joblib.load("model/home_encoder.pkl")
away_encoder = joblib.load("model/away_encoder.pkl")
tour_encoder = joblib.load("model/tour_encoder.pkl")

# ---------------- HEADER ----------------
st.image(
    "https://upload.wikimedia.org/wikipedia/en/thumb/f/f3/FIFA_World_Cup_2022.svg/800px-FIFA_World_Cup_2022.svg.png",
    width=150
)

st.title("🏆 FIFA World Cup Predictor")
st.subheader("Predict Match Results Using Machine Learning")

st.markdown("---")

# ---------------- TEAM SELECTION ----------------
col1, col2 = st.columns(2)

with col1:
    home_team = st.selectbox(
        "⚽ Home Team",
        home_encoder.classes_
    )

with col2:
    away_team = st.selectbox(
        "⚽ Away Team",
        away_encoder.classes_
    )

# ---------------- TOURNAMENT ----------------
tournament = st.selectbox(
    "🏟 Tournament",
    tour_encoder.classes_
)

st.markdown("")
st.markdown("---")
st.subheader("⭐ Team Captains")

col1, col2 = st.columns(2)

with col1:

    st.markdown(f"### 🏠 {home_team}")

    if home_team in captains:

        captain = captains[home_team]

        st.image(
            captain["image"],
            width=220
        )

        st.markdown(
            f"""
            <div class="captain-card">
                <h3>{captain['name']}</h3>
                <p>{captain['role']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        st.info("Captain information not available")


with col2:

    st.markdown(f"### ✈ {away_team}")

    if away_team in captains:

        captain = captains[away_team]

        st.image(
            captain["image"],
            width=220
        )

        st.markdown(
            f"""
            <div class="captain-card">
                <h3>{captain['name']}</h3>
                <p>{captain['role']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        st.info("Captain information not available")
# ---------------- PREDICT BUTTON ----------------
if st.button("🏆 Predict Winner", use_container_width=True):

    home_encoded = home_encoder.transform(
        [home_team]
    )[0]

    away_encoded = away_encoder.transform(
        [away_team]
    )[0]

    tournament_encoded = tour_encoder.transform(
        [tournament]
    )[0]

    prediction = model.predict(
        [[home_encoded,
          away_encoded,
          tournament_encoded]]
    )[0]

    st.balloons()

    st.markdown("## 🎯 Match Prediction")

    if prediction == "Win":

        st.markdown(
            f"""
            <div class="result-box">
            🏆 {home_team} is predicted to WIN!
            </div>
            """,
            unsafe_allow_html=True
        )

    elif prediction == "Loss":

        st.markdown(
            f"""
            <div class="result-box">
            🏆 {away_team} is predicted to WIN!
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="result-box">
            🤝 {home_team} vs {away_team}<br>
            Predicted Result: DRAW
            </div>
            """,
            unsafe_allow_html=True
        )

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Built with Python • Scikit-Learn • Streamlit")