import React from 'react'

const AuthorItem = ({author}) => {
return(
    <tr>
        <td>
            {author.first_name}
        </td>
        <td>
            {author.last_name}
        </td>
        <td>
            {author.birthday}
        </td>
    </tr>
)}

const AuthorList = ({authors}) => {
    return(
        <table>
            <thead>
                <tr>
                    <th>
                        name
                    </th>
                    <th>
                        fam
                    </th>
                    <th>
                        birthday
                    </th>
                </tr>
            </thead>
            {authors.map((author) => <AuthorItem author={author} />)}
        </table>
        )
}

export default AuthorList