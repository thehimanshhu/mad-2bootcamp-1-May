<template>
    <div v-if="professional">
        <div class="card mt-5 ms-5 me-5 mb-3">
            <div class="card-body">
                <h1>{{ professional.name }}</h1>
                <h3>{{ professional.email }}</h3>
            </div>
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
                        <tr v-for="(pack, index) in professional.packages" :key="index">
                            <td>{{ pack.name }}</td>
                            <td>{{ pack.price }}</td>


                            <td class="d-flex gap-2">
                                <router-link :to="`/view-package/${pack.id}`" class="btn btn-primary">View</router-link>
                               
                            </td>
                        </tr>
                    </tbody>
                </table>

            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "ViewProfessional",
    data() {
        return {
            prof_id: null,
            professional: null

        }
    },
    methods: {
        async getProfessional() {
            try {
                const response = await fetch(`http://localhost:5000/get-professional?prof_id=${this.prof_id}`, {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json",
                        "Authentication-Token": localStorage.getItem("token")
                    },
                })
                const data = await response.json()
                if (response.status == 200) {
                    this.professional = data
                    console.log(this.professional)
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
                    this.$router.push("/admin/dashboard")
                }
            }
            catch (error) {
                console.log(error.message)
                this.$router.go(0)
            }
        }
    },
    mounted() {
        this.prof_id = this.$route.params.id
        this.getProfessional()
    }
}

</script>