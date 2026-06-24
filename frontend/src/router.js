import {createRouter , createWebHistory}  from "vue-router"
import Home from "./components/Home.vue"
import Login from "./components/Login.vue"
import Register from "./components/Register.vue"
import AdminDashboard from "./components/Admin/Dashboard.vue"
import CustomerDashboard from "./components/Customer/Dashboard.vue"
import ProfessionalDashboard from "./components/Professional/Dashboard.vue"
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
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes

})
export default router