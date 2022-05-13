import pandas as pd
import streamlit as st
from sklearn.metrics import jaccard_score
from scipy.spatial.distance import pdist, squareform

# data importing
data = pd.read_csv('Product.csv')
df = pd.DataFrame(data=data)
df.drop(columns=['Unnamed: 0', 'Userid'], inplace=True)
array_df = pd.crosstab(df['Product'], df['Mailid'], )
array_df = pd.DataFrame(array_df)

jaccard_distance = pdist(array_df.values, metric='jaccard')
jaccard_distance_square = squareform(jaccard_distance)
jaccard_similarity_array = 1 - jaccard_distance_square
distance_df = pd.DataFrame(jaccard_similarity_array, index=array_df.index, columns=array_df.index)




def main():
    st.title("Product Recommendation System")
    st.write("Banking Products")
    st.write(df[['Product', 'Mailid']].head())
    st.write(" ")
    mailid = st.text_input("Enter you mailid")
    if st.button("Enter"):
        st.write(" ")
        if mailid in list(df["Mailid"].unique()):
            st.write("Welcome back!")
            df.set_index(['Mailid'], inplace=True)
            i = df[df.index == mailid]
            last_product = len(i['Product'].values)
            val = i['Product'].values[last_product - 1]
            st.write("your current product:", val)
            st.write("#### Products you may like ")
            col1, col2, col3 = st.columns(3)
            rec_pro = (distance_df[val].sort_values(ascending=False))
            list1 = []
            for final_prouduct in rec_pro[1:4].index:
                list1.append(final_prouduct)
            with col1:
                st.write(list1[0])

            with col2:
                st.write(list1[1])

            with col3:
                st.write(list1[2])
        else:
            st.write("User not found!")

    st.write(" ")
    st.write("Project by Bhuvaneshwar A")


if __name__ == "__main__":
    main()
