import 'babel-polyfill';
import React from 'react';

import {Button, Header, Container, Grid} from 'semantic-ui-react'

type ItemProps = {
    name: string,
    description: string
}

class Item extends React.Component<ItemProps> {
    props: ItemProps;

    render(): React.Node {
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

type AppProps = {}

type AppState = {
    my_objects: Array<Object>
}

class App extends React.Component<AppProps, AppState> {

    constructor(props: Object) {
        super(props);
        this.state = {
            my_objects: [],
        };
    }

    async loadObjects() {

        let my_options = {
            'credentials': 'include'
        };
        this.setState({
            my_objects: await fetch('/api/list.json', my_options).then(response => response.json())
        })
    }

    componentDidMount() {
        this.loadObjects();
    }

    render() {



        return (
            <div>
                <Grid>
                    {this.state.my_objects.map( (obj, i) => (
                            <Grid.Row key={i}>
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