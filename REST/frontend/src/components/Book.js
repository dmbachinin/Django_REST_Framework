import React from 'react'

const BookItem = ({item}) => {
return(
    <tr>
        <td>
            {item.name}
        </td>
        <td>
            {item.author[0].first_name}
        </td>
    </tr>
)}

const BookList = ({items}) => {
    return(
        <table>
            <thead>
                <tr>
                    <th>
                        Name
                    </th>
                    <th>
                        Author
                    </th>
                </tr>
            </thead>
            {items.map((item) => <BookItem item={item} />)}
        </table>
        )
}

export default BookList