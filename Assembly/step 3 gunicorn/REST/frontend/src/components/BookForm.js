import React from 'react'


class BookForm extends React.Component{

    constructor(props){
        super(props)
        this.state = {name: '', author: props.authors[0]?.id}
    }
    // Событие изменения формы
    handleChange(event){
        this.setState(
            {[event.target.name]: event.target.value} // Запись данных в state при завписи их в поля для ввода
        );
    }

    handleSubmit(event){
        this.props.createBook(this.state.name, this.state.author)
        event.preventDefault() // Отключает отправку формы  при нажатии на кнопку
    }

    render() {
        return(
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className='form-group'>
                    <label for='name'>name</label>
                    <input type='text' className='form-control' name='name' value={this.state.name} onChange={(event)=>this.handleChange(event)} />
                </div>
                <div className='form-group'>
                    <label for='author'>author</label>
                    <select className='form-control' name='author' value={this.state.author} onChange={(event)=>this.handleChange(event)}>
                        {this.props.authors.map((item)=> <option value={item.id}>{item.first_name}</option>)}
                    </select>
                </div>
                <input type='submit' className='btn btn-primary' value='Save'/>
            </form>
        );
    }
}

export default BookForm
