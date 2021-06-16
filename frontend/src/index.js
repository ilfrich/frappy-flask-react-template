import React from "react"
import { render } from "react-dom"
import { BrowserRouter } from "react-router-dom"
import { withRouter, Switch, Route } from "react-router"
import { LoginWrapper, UserManager, PermissionCheck } from "@frappy/react-authentication"
import { DataSetManager } from "@frappy/react-datasets"
import { ContentManager } from "@frappy/react-content"
import LandingPage from "./containers/LandingPage"

const style = {
    main: {
         maxWidth: "1280px",
         margin: "auto",
         padding: "30px",
    },
    // alternative for full width
//    main: {
//         width: "100%"
//         padding: "30px",
//    },
}

// define your routes here
const RouterApp = withRouter(props => (
    <div>
        {/* add header here before the main and add top margin to style.main above */}
        <div style={style.main}>
            <Switch>
                <Route path="/" exact component={() => <LandingPage currentUser={props.currentUser} />} />
                <Route
                    path="/admin/user"
                    exact
                    component={() => (
                        <PermissionCheck currentUser={props.currentUser} requiredPermissions="admin" showError>
                            <UserManager currentUser={props.currentUser} permissions={["data", "content"]} />
                        </PermissionCheck>
                    )}
                />
                <Route
                    path="/admin/data"
                    exact
                    component={() => (
                        <PermissionCheck currentUser={props.currentUser} requiredPermissions="data" showError>
                            <DataSetManager
                                currentUser={props.currentUser}
                                assignments={{
                                    assignmentKey1: {
                                        label: "Assignment Object #1",
                                        dataTypes: ["type1", "type2", "type3"],
                                    },
                                }}
                            />
                        </PermissionCheck>
                    )}
                />
                <Route
                    path="/admin/content"
                    exact
                    component={() => (
                        <PermissionCheck currentUser={props.currentUser} requiredPermissions="content" showError>
                            <ContentManager
                                currentUser={props.currentUser}
                                references={["demo1", "demo2"]}
                                contentTypes={{
                                    description: {
                                        list: false,
                                        fields: ["title", "description"],
                                    },
                                    team: {
                                        list: true,
                                        fields: ["name", "role"],
                                    },
                                }}
                            />
                        </PermissionCheck>
                    )}
                />
            </Switch>
        </div>
    </div>
))


// wraps the router
class RouterWrapper extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            currentUser: null,
        }
        this.setUser = this.setUser.bind(this)
    }

    setUser(user) {
        this.setState({
            currentUser: user,
        })
    }

    render() {
        return(
            <BrowserRouter>
                <LoginWrapper setUser={this.setUser}>
                    <RouterApp currentUser={this.state.currentUser} />
                </LoginWrapper>
            </BrowserRouter>
        )

    }
}

// main entry point for the frontend
render(<RouterWrapper />, document.getElementById("root"))
