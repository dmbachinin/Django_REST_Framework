import React from 'react'

import './App.css';
import AuthorList from './components/Author.js'

class App extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            'authors': []
        }
    }
    componentDidMount() {
        const authors = [
            {
                'first_name': 'Dima',
                'last_name': 'Balanchine',
                'birthday': 2003
            },
            {
                'first_name': 'Anna',
                'last_name': 'Burkina',
                'birthday': 2003
            },
            {
                'first_name': 'Olga',
                'last_name': 'Machina',
                'birthday': 1996
            },
        ]
        this.setState(
            {
                'authors': authors
            }
        )
    }
    render() {
    console.log(this.state.authors)
        return (
        <div>
            <AuthorList authors={this.state.authors}/>
        </div>
        )
    }
}

export default App;
