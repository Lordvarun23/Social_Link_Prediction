import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")


def About():
    st.header("Facebook Link Prediction Challenge")
    st.write("This project is based on social media link prediction whether two users are going to be friend in future or not.")
    st.subheader("Dataset:")
    st.markdown("Taken data from facebook's recruting challenge on kaggle in graph<style><br> <ol><li>source_node int64</li><li>destination_node int64</li><li>source_node int64</li></ol></style>",unsafe_allow_html=True)
    Img1 = Image.open("Images/network.png")
    st.image(Img1,caption="Sample Subgraph")
    st.subheader("Mapping the problem into supervised learning problem:")
    st.write("Generated training samples of good and bad links from given directed graph and for each link got some features like no of followers, is he followed back, page rank, katz score, adar index, some svd fetures of adj matrix, some weight features etc. and trained ml model based on these features to predict link.")


def EDA():
    st.header("Exploratory Data Analysis")
    st.subheader("Followers")
    Img2 = Image.open("Images/no_of.png")
    st.image(Img2,caption="No of Followers")
    Img3 = Image.open("Images/download.png")
    st.image(Img3, caption="No of Followers at 99%")
    Img4 = Image.open("Images/download (4).png")
    st.image(Img4, caption="Distribution of no of followers")
    st.subheader("Following Plots")
    Img5 = Image.open("Images/download (2).png")
    st.image(Img5, caption="No of Following of each person")
    Img6 = Image.open("Images/download (3).png")
    st.image(Img6, caption="No of Followings at 99%")
    Img7 = Image.open("Images/download (1).png")
    st.image(Img7, caption="Distribution of no of following")


def Results():
    st.header("Modelling")
    st.subheader("We have used Random Forest Classifier Technique")
    st.subheader("Columns")
    st.markdown(['source_node', 'destination_node', 'indicator_link',
       'jaccard_followers', 'jaccard_followees', 'cosine_followers',
       'cosine_followees', 'num_followers_s', 'num_followees_s',
       'num_followees_d', 'inter_followers', 'inter_followees', 'adar_index',
       'follows_back', 'same_comp', 'shortest_path', 'weight_in', 'weight_out',
       'weight_f1', 'weight_f2', 'weight_f3', 'weight_f4', 'page_rank_s',
       'page_rank_d', 'katz_s', 'katz_d', 'hubs_s', 'hubs_d', 'authorities_s',
       'authorities_d', 'svd_u_s_1', 'svd_u_s_2', 'svd_u_s_3', 'svd_u_s_4',
       'svd_u_s_5', 'svd_u_s_6', 'svd_u_d_1', 'svd_u_d_2', 'svd_u_d_3',
       'svd_u_d_4', 'svd_u_d_5', 'svd_u_d_6', 'svd_v_s_1', 'svd_v_s_2',
       'svd_v_s_3', 'svd_v_s_4', 'svd_v_s_5', 'svd_v_s_6', 'svd_v_d_1',
       'svd_v_d_2', 'svd_v_d_3', 'svd_v_d_4', 'svd_v_d_5', 'svd_v_d_6'])
    st.subheader("Hyper-Parameter Tuning")
    Img1 = Image.open("Images/download (5).png")
    st.image(Img1,caption="No of Estimators parameter tuning")
    Img2 = Image.open("Images/download (6).png")
    st.image(Img2,caption="Depth parameter tuning")
    st.subheader("Random Forest Performace metrics")
    Img3 = Image.open("Images/download (7).png")
    st.image(Img3,caption="Train Confusion Matrix")
    Img4 = Image.open("Images/download (8).png")
    st.image(Img4, caption="Test Confusion Matrix")
    Img5 = Image.open("Images/download (9).png")
    st.image(Img5, caption="ROC Curve for Test Data")
    st.subheader("Feature Importance")
    Img6 = Image.open("Images/download (10).png")
    st.image(Img6, caption="Feature Importance")

def Resources():
    st.subheader("Resources used:")
    st.write("1. https://storage.googleapis.com/kaggle-forum-message-attachments/2594/supervised_link_prediction.pdf")
    st.write("2. Kaggle")

    st.subheader("Contact:")
    st.write("Varun S (Varunkavin5@gmail.com), Venu H(20pd08@psgtech.ac.in")

    st.subheader("Code Repo: Github(https://github.com/Lordvarun23)")

page = st.sidebar.selectbox('Select page', ['About', 'EDA', 'Results','Resources'])
if page == 'About':
    About()
elif page== 'EDA':
    EDA()
elif page == 'Results':
    Results()
else:
    Resources()