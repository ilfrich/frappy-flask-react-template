import React from "react"
import { Outlet } from "react-router-dom"

const Header = ({ currentUser }) => (
    <>
        <div>
            Header
        </div>
        <Outlet />
    </>

)

export default Header