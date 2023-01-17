import React from 'react'

import {Link} from 'react-router-dom'

const AuthorItem = ({author}) => {
return(
    <tr>
        <td>
            <Link to={`author/${author.id}`}>{author.id}</Link>
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