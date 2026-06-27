import {createRouter , createWebHistory}  from "vue-router"
import Home from "./components/Home.vue"
import Login from "./components/Login.vue"
import Register from "./components/Register.vue"
import AdminDashboard from "./components/Admin/Dashboard.vue"
import CustomerDashboard from "./components/Customer/Dashboard.vue"
import ProfessionalDashboard from "./components/Professional/Dashboard.vue"
import LogOut from "./components/LogOut.vue"
import CreatePackage from "./components/Professional/CreatePackage.vue"
import ViewPackage from "./components/Professional/ViewPackage.vue"
import ViewProfessional from "./components/Admin/viewProfessional.vue"
import BookPackage from "./components/Customer/bookPackage.vue"
import Search from "./components/Admin/Search.vue"
const routes = [
    {
        path : "/" , component : Home  
    },
    {
        path: "/login" , component : Login
    },
    {
        path : "/register" , component: Register
    },
    {
        path : "/admin/dashboard" , component: AdminDashboard
    },
    {
        path : "/customer/dashboard" , component: CustomerDashboard
    },
    {
        path : "/professional/dashboard" , component: ProfessionalDashboard
    },
    {
        path : "/logout" , component: LogOut
    },
    {
        path : "/create-package" , component: CreatePackage
    },
    {
        path : "/view-package/:id" , component: ViewPackage
    },
    {
        path : "/view-professional/:id" , name:"ViewProfessional" , component: ViewProfessional
    },
    {
        path : "/book-package/:id"  , component: BookPackage
    },
    {
        path : "/search"  , component: Search
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes

})
export default router