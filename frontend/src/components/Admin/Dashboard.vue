<template>
    <NavBar></NavBar>
    <div class="card mt-5 ms-5 me-5">
        <div class="card-header">
            Professionals
        </div>
        <div class="card-body">
            <table class="table border">
                <thead>
                    <tr>

                        <th scope="col">Name</th>
                        <th scope="col">Email</th>
                        <th scope="col">Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(prof, index) in prof_list" :key="index">
                        <td>{{ prof.name }}</td>
                        <td>{{ prof.email }}</td>
                        <td>
                            <router-link :to="`/view-professional/${prof.id}` " class="btn btn-primary">View</router-link>
                        </td>
                    </tr>
                </tbody>
            </table>

        </div>
    </div>
    <div class="card mt-5 ms-5 me-5">
        <div class="card-header">
            Customers
        </div>
        <div class="card-body">
            <table class="table border">
                <thead>
                    <tr>

                        <th scope="col">Name</th>
                        <th scope="col">Email</th>
                        <th scope="col">Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(cust, index) in cust_list" :key="index">
                        <td>{{ cust.name }}</td>
                        <td>{{ cust.email }}</td>
                        <td></td>
                    </tr>
                </tbody>
            </table>

        </div>
    </div>

</template>

<script>

import NavBar from '../NavBar.vue';
export default {
    name: "AdminDashComp",

    data() {
        return {
            prof_list: null,
            cust_list: null

        }
    },
    methods: {
        async fetchProfessional() {
            try {
                const response = await fetch("http://localhost:5000/list-professionals", {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json",
                        "Authentication-Token": localStorage.getItem("token")
                    },
                })
                const data = await response.json()
                if (response.status == 200) {
                    this.prof_list = data
                    console.log(this.prof_list)
                }
                else if (response.status == 401) {
                    console.log("you are not logged in please login")
                    this.$router.push("/logout")
                }
                else if (response.status == 403) {
                    console.log("you don't have access to view this resource.")
                    this.$router.push("/logout")
                }
            }
            catch (error) {
                console.log(error.message)
                this.$router.go(0)
            }
        },
        async fetchCustomers() {
            try {
                const response = await fetch("http://localhost:5000/list-customers", {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json",
                        "Authentication-Token": localStorage.getItem("token")
                    },
                })
                const data = await response.json()
                if (response.status == 200) {
                    this.cust_list = data
                    console.log(this.cust_list)
                }
                else if (response.status == 401) {
                    console.log("you are not logged in please login")
                    this.$router.push("/logout")
                }
                else if (response.status == 403) {
                    console.log("you don't have access to view this resource.")
                    this.$router.push("/logout")
                }
            }
            catch (error) {
                console.log(error.message)
                this.$router.go(0)
            }
        }
    },
    mounted() {
        this.fetchProfessional()
        this.fetchCustomers()
    },
    components: {
        NavBar
    }
}

</script>