import React from 'react'
import axios from 'axios'

import './App.css';
import AuthorList from './components/Author.js'
import BookList from './components/Book.js'
import AuthorBookList from './components/AuthorBook.js'

import {HashRouter, Route, Link, Switch,Redirect,BrowserRouter} from 'react-router-dom'

const NotFound404 = ({location}) => {
    return (
    <div>
        <h1>Страница по адресу `{location.pathname}` недоступна</h1>
    </div>
    )
}

class App extends React.Component{
    constructor(props){
        super(props)

        const authors = [
            {
                id: 1,
                first_name: "Dima",
                last_name: "Bachinin",
                birthday: "2003"
            },{
                id: 2,
                first_name: "Anna",
                last_name: "Azbukina",
                birthday: "2003"
            }
        ]

        const books = [
            {
                id: 1,
                name: "Как любить?",
                author: authors[1]
            },{
                id: 2,
                name: "КАК СРАТЬ?",
                author: authors[0]
            },
            {
                id: 3,
                name: "Как любить 2?",
                author: authors[1]
            },{
                id: 4,
                name: "КАК СРАТЬ 2?",
                author: authors[0]
            },
        ]

        this.state = {
            'authors': authors,
            'books': books
        }
    }

//    componentDidMount() {
//        axios.get('http://127.0.0.1:8000/api/authors').then(
//            response => {
//                this.setState(
//                    {
//                        'authors': response.data
//                    }
//                )
//            }
//        ).catch(error => console.log(error))
//    }
    render() {
        return (
        <div className='App'>
            <BrowserRouter>
                <nav>
                    <ul>
                        <li>
                            <Link to = '/'>Авторы</Link>
                        </li>
                        <li>
                            <Link to = '/books'>Книги</Link>
                        </li>
                    </ul>
                </nav>
                <Switch>
                    <Route exact path='/' component={ ()=> <AuthorList authors={this.state.authors} /> } />
                    <Route exact path='/books' component={ ()=>  <BookList items={this.state.books}/ > } />
                    <Route exact path='/author/:id' component={ ()=>  <AuthorBookList items={this.state.books}/ > } />
                    <Redirect from='/authors' to = '/'/>
                    <Route component={ NotFound404 } />
                </Switch>
            </BrowserRouter>
        </div>
        )
    }
}

export default App;
