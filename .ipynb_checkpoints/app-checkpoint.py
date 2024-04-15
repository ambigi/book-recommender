import numpy as np
import streamlit as st
import pickle

pt=pickle.load(open('pt.pkl','rb'))
sim=pickle.load(open('similarity.pkl','rb'))
books=pickle.load(open('book_list.pkl','rb'))
book_list=books['Book-Title'].values
st.header('Book Recommender System')
select_value=st.selectbox('Select Book from dropdown',book_list)


def recommend(book_name):
    # index fetch
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(sim[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)
    return data


if st.button('Show Recommendations'):
    book_name=recommend(select_value)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(book_name[0][0])
        st.image(book_name[0][2])
    with col2:
        st.text(book_name[1][0])
        st.image(book_name[1][2])
    with col3:
        st.text(book_name[2][0])
        st.image(book_name[2][2])
    with col4:
        st.text(book_name[3][0])
        st.image(book_name[3][2])