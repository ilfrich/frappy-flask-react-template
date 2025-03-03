import React from "react"
import { RouterProvider, createBrowserRouter } from "react-router-dom"
import { createRoot } from "react-dom/client"
import { LoginWrapper, UserManager, PermissionCheck } from "@frappy/react-authentication"
import LandingPage from "./containers/LandingPage"
import Header from "./components/layout/Header"

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

        // define routes here
        const routers = createBrowserRouter([
            {
                element: (
                    <Header currentUser={this.state.currentUser} />
                ),
                children: [
                    {
                        path: "/",
                        element: <LandingPage currentUser={this.state.currentUser} />
                    },
                    {
                        path: "/admin/users",
                        element: (
                            <PermissionCheck currentUser={this.state.currentUser} requiredPermissions="admin" showError>
                                <UserManager currentUser={this.state.currentUser} permissions={["data", "content"]} />
                            </PermissionCheck>
                        )
                    }
                ]

            }
        ])

        return(
            <LoginWrapper setUser={this.setUser}>
                <div style={style.main}>
                    <RouterProvider router={routers} />
                </div>
            </LoginWrapper>
        )

    }
}

// main entry point for the frontend
createRoot(document.getElementById("root")).render(<RouterWrapper />)