/* ===========================================
   SIPETA PROFESSIONAL STYLE
=========================================== */

/* Font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}

/* ===========================
   MAIN
=========================== */

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    padding-left:3rem;
    padding-right:3rem;
}

/* ===========================
   SIDEBAR
=========================== */

[data-testid="stSidebar"]{
    background:#1B5E20;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label{
    color:white;
}

[data-testid="stSidebarNav"]{
    background:#1B5E20;
}

[data-testid="stSidebarNav"] a{
    border-radius:12px;
    margin-bottom:6px;
}

[data-testid="stSidebarNav"] a:hover{
    background:#2E7D32;
}

/* ===========================
   TITLE
=========================== */

h1{
    color:#2E7D32;
    font-weight:700;
}

h2{
    color:#388E3C;
}

h3{
    color:#388E3C;
}

/* ===========================
   BUTTON
=========================== */

.stButton>button{

    background:#2E7D32;
    color:white;

    border:none;

    border-radius:10px;

    font-weight:600;

    transition:0.3s;

    width:100%;
}

.stButton>button:hover{

    background:#43A047;

    transform:scale(1.02);

}

/* ===========================
   INPUT
=========================== */

.stTextInput input{

    border-radius:10px;

}

.stNumberInput input{

    border-radius:10px;

}

.stSelectbox div{

    border-radius:10px;

}

/* ===========================
   METRIC
=========================== */

[data-testid="metric-container"]{

    background:white;

    border-radius:15px;

    padding:20px;

    box-shadow:0 4px 15px rgba(0,0,0,.08);

    border-left:6px solid #2E7D32;

}

/* ===========================
   DATAFRAME
=========================== */

[data-testid="stDataFrame"]{

    border-radius:15px;

    overflow:hidden;

}

/* ===========================
   INFO SUCCESS WARNING
=========================== */

.stAlert{

    border-radius:12px;

}

/* ===========================
   CARD
=========================== */

.card{

    background:white;

    border-radius:15px;

    padding:20px;

    box-shadow:0 6px 20px rgba(0,0,0,.08);

    margin-bottom:20px;

}

/* ===========================
   FOOTER
=========================== */

.footer{

    text-align:center;

    padding:20px;

    color:gray;

    margin-top:50px;

}

/* ===========================
   LOGIN
=========================== */

.login-box{

    max-width:550px;

    margin:auto;

    background:white;

    padding:40px;

    border-radius:20px;

    box-shadow:0 10px 25px rgba(0,0,0,.15);

}

/* ===========================
   IMAGE
=========================== */

img{

    border-radius:12px;

}

/* ===========================
   TAB
=========================== */

.stTabs{

    border-radius:10px;

}

/* ===========================
   EXPANDER
=========================== */

.streamlit-expanderHeader{

    font-weight:600;

}

/* ===========================
   PLOTLY
=========================== */

.js-plotly-plot{

    border-radius:15px;

}

/* ===========================
   DIVIDER
=========================== */

hr{

    border:1px solid #E0E0E0;

}

/* ===========================
   SCROLLBAR
=========================== */

::-webkit-scrollbar{

    width:10px;

}

::-webkit-scrollbar-thumb{

    background:#43A047;

    border-radius:20px;

}

/* ===========================
   ANIMATION
=========================== */

[data-testid="metric-container"],
.stButton>button,
.card{

    transition:.3s;

}

[data-testid="metric-container"]:hover,
.card:hover{

    transform:translateY(-3px);

    box-shadow:0 10px 25px rgba(0,0,0,.15);

}