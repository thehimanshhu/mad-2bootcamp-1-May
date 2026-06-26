<template>
    <div v-if="pack">
        <div class="card mt-5 ms-5 me-5 mb-3">
            <div class="card-body">
                <h1>{{ pack.name }}</h1>
                <h3>{{ pack.price }}</h3>
            </div>
        </div>
        <div class="card ms-5 me-5">
            <div class="card-header">
                Bookings
            </div>
            <div class="card-body">
                <table class="table border">
                    <thead>
                        <tr >

                            <th scope="col">Customer Name</th>
                            <th scope="col">Customer Email</th>
                            <th scope="col">Date</th>
                            <th scope="col">Time</th>
                            <th scope="col">Status</th>
                            <th scope="col">Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(booking, index) in pack.bookings" :key="index">
                            <td>{{ booking.customer_name }}</td>
                            <td>{{ booking.customer_email }}</td>
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
    </div>
</template>

<script>
export default {
    name: "ViewPackage",
    data() {
        return {
            pack_id: null,
            pack: null

        }
    },
    methods: {
        async getPackage() {
            try {
                const response = await fetch(`http://localhost:5000/get-package?pack_id=${this.pack_id}`, {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json",
                        "Authentication-Token": localStorage.getItem("token")
                    },
                })
                const data = await response.json()
                if (response.status == 200) {
                    this.pack = data
                    console.log(this.pack)
                }
                else if (response.status == 401) {
                    console.log("you are not logged in please login")
                    this.$router.push("/logout")
                }
                else if (response.status == 403) {
                    console.log("you don't have access to view this resource.")
                    this.$router.push("/logout")
                }
                else if (response.status == 404) {
                    console.log("you don't have access to view this resource.")
                    this.$router.push("/professional/dashboard")
                }
            }
            catch (error) {
                console.log(error.message)
                this.$router.go(0)
            }
        },
    },
    mounted() {
        this.pack_id = this.$route.params.id
        this.getPackage()
    }
}

</script>