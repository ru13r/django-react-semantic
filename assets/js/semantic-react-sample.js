import React from 'react';
import {Button, Header, Container, Segment, Grid} from 'semantic-ui-react'


class Item extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <Container text>
                <Header content={this.props.name}/>
                <p>
                    {this.props.description}
                </p>
                <Button content='read more...' primary/>
            </Container>

        )
    }
}

class App extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            my_objects: [],
            number: 0
        };
    }

    async loadObjects() {

        let my_options = {
            "credentials": "include"
        };
        this.setState({
            my_objects: await fetch("/api/list.json", my_options).then(response => response.json())
        })
    }

    componentDidMount() {
        this.loadObjects();
    }

    render() {
        return (
            <div>
                <Grid>
                    {this.state.my_objects.map(obj => (
                            <Grid.Row>
                                <Item name={obj.name} description={obj.description}/>
                            </Grid.Row>
                        )
                    )}
                </Grid>
            </div>

        )
    }
}

export default App;