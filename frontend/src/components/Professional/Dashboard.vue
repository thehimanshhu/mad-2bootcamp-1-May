<template>
    <NavBar></NavBar>
    <div v-if="message" class="alert alert-success mt-2" role="alert">
       {{ message }}
    </div>

    <div class="card mt-5 ms-5 me-5">
        <div class="card-header d-flex">
            Packages
            <router-link to="/create-package" class="btn btn-warning ms-auto">Create</router-link>
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
                            <router-link :to="`/view-package/${pack.id}`" class="btn btn-primary">View</router-link>
                            <button class="btn btn-danger" @click="deletePack(pack.id)">Delete</button>
                        </td>
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
            message:null
        }
    },
    methods: {
        async fetchPackages() {
            try {
                const response = await fetch("http://localhost:5000/list-packages", {
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
        async deletePack(packageId) {
            console.log("hellllllllś")
            try {
                const response = await fetch(`http://localhost:5000/delete-package?pack-id=${packageId}`, {
                    method: "DELETE",
                    headers: {
                        "Content-Type": "application/json",
                        "Authentication-Token": localStorage.getItem("token")
                    },

                })
                const data = await response.json()
                if (response.status == 200) {
                    this.message=data.message
                    this.fetchPackages()
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
                    console.log("the resource doesn't exist.")
                    this.message = data.message
                }
            }
            catch (error) {
                console.log(error.message)
                this.$router.go(0)
            }
        }

    },
    components: {
        NavBar
    },
    mounted() {
        this.fetchPackages()
    }
}

</script>