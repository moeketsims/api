import React, { Component } from 'react'
import axios from 'axios'

class DjangoAPI extends Component {

    constructor(props) {
        super(props);

        this.state = {
            lists:[]
        }
    }
    
    componentDidMount(){

        axios.get('http://127.0.0.1:8000/api/upload/')
        .then(response => {
            console.log(response)
            this.setState({
                lists: response.data
            })
        })
        .catch(error => {
            console.log(error)
        })
    }


    render() {
        const {lists } = this.state
        return (
            <div>
                Testing if the class works
                {
                    lists.length?
                    lists.map(post => <div key={post.id}>{post.source} and {post.source}</div>):
                    null
                }   
            </div>
        );
    }
}

export default DjangoAPI;