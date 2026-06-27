<template>
    <NavBar></NavBar>
    <div v-if="message" class="alert alert-success mt-2" role="alert">
        {{ message }}
    </div>

    <div class="card mt-5 ms-5 me-5">
        <div class="card-header d-flex">
            Packages

        </div>
        <div class="card-body">
            <table class="table border">
                <thead>
                    <tr>

                        <th scope="col">Name</th>
                        <th scope="col">Price</th>

                        <th scope="col">Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(pack, index) in package_list" :key="index">
                        <td>{{ pack.name }}</td>
                        <td>{{ pack.price }}</td>


                        <td class="d-flex gap-2">
                            <router-link :to="`/book-package/${pack.id}`" class="btn btn-primary">Book</router-link>

                        </td>
                    </tr>
                </tbody>
            </table>

        </div>
    </div>
    <div class="card ms-5 me-5 mt-3 mb-3">
        <div class="card-header">
            Bookings
        </div>
        <div class="card-body">
            <table v-if="bookings" class="table border">
                <thead>
                    <tr>

                        <th scope="col">Professional Name</th>
                        <th scope="col">Professional Email</th>
                        <th scope="col">Package</th>
                        <th scope="col">Date</th>
                        <th scope="col">Time</th>
                        <th scope="col">Status</th>
                        <th scope="col">Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(booking, index) in bookings" :key="index">
                        <td>{{ booking.professional_name }}</td>
                        <td>{{ booking.professional_email }}</td>
                        <td>{{ booking.package_name }}</td>
                        <td>{{ booking.date }}</td>
                        <td>{{ booking.time }}</td>
                        <td>{{ booking.status }}</td>
                        <!-- <td class="d-flex gap-2">
                                <button class="btn btn-primary">View</button>
                                <button class="btn btn-danger" @click="deletePack(pack.id)">Delete</button>
                            </td> -->
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import NavBar from '../NavBar.vue';
export default {
    name: "ProfessinalDashComp",
    data() {
        return {
            package_list: null,
            message: null,
            bookings : null
        }
    },
    methods: {
        async fetchPackages() {
            try {
                const response = await fetch("http://localhost:5000/get-packages", {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json",
                        "Authentication-Token": localStorage.getItem("token")
                    },
                })
                const data = await response.json()
                if (response.status == 200) {
                    this.package_list = data
                    console.log(this.package_list)
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
        async getBookings() {
            try {
                const response = await fetch("http://localhost:5000/get-bookings", {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json",
                        "Authentication-Token": localStorage.getItem("token")
                    },
                })
                const data = await response.json()
                if (response.status == 200) {
                    this.bookings = data

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

    },
    components: {
        NavBar
    },
    mounted() {
        this.fetchPackages()
        this.getBookings()
    }
}

</script>