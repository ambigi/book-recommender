import numpy as np
import streamlit as st
import pickle

pt=pickle.load(open('pt.pkl','rb'))
sim=pickle.load(open('similarity.pkl','rb'))
books=pickle.load(open('book_list.pkl','rb'))
popular_books=pickle.load(open('popular_books.pkl','rb'))
book_list=books['Book-Title'].values
st.header('Book Recommender System')
select_value=st.selectbox('Select Book from dropdown',book_list)


def recommend(book_name):
    # index fetch
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(sim[index])), key=lambda x: x[1], reverse=True)[1:6]

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
        st.text(book_name[0][1])
    with col2:
        st.text(book_name[1][0])
        st.image(book_name[1][2])
        st.text(book_name[1][1])
    with col3:
        st.text(book_name[2][0])
        st.image(book_name[2][2])
        st.text(book_name[2][1])
    with col4:
        st.text(book_name[3][0])
        st.image(book_name[3][2])
        st.text(book_name[3][1])
    with col5:
        st.text(book_name[4][0])
        st.image(book_name[4][2])
        st.text(book_name[4][1])

st.write("### 50 TOP RATED BOOKS")

images_per_row = 5
row_spacing = 1

# Calculate the number of rows needed
num_rows = -(-len(popular_books) // images_per_row)  #Equivalent to math.ceil(len(popular_books) / images_per_row)

# Display images in rows with specified number of columns
for i in range(num_rows):
    # Create a row with multiple columns
    row = st.columns(images_per_row)

    # Iterate over images in the current row
    for j in range(images_per_row):
        index = i * images_per_row + j
        if index < len(popular_books):
            row[j].text(popular_books['Book-Title'][index])
            row[j].image(popular_books['Image-URL-M'][index])
            row[j].text(popular_books['Book-Author'][index])
    st.write("")
    st.write("---" * row_spacing)
