<template>
    <div class="d-flex justify-content-center mt-5">
        <div class="card " style="width: 23rem;">
            <div class="card-body">
                <div class="d-flex">
                    <div class="form-check me-3">
                        <input class="form-check-input" type="radio" v-model="formdata.query_type" name="radioDefault"
                            id="radioDefault1"   value="prof"  >
                        <label class="form-check-label" for="radioDefault1">
                            Professional
                        </label>
                    </div>
                    <div class="form-check me-3">
                        <input class="form-check-input" type="radio" name="radioDefault" v-model="formdata.query_type"
                            id="radioDefault2" value="cust">
                        <label class="form-check-label" for="radioDefault2">
                            Customer
                        </label>
                    </div>
                    <div class="form-check">
                        <input class="form-check-input" type="radio" name="radioDefault" v-model="formdata.query_type"
                            id="radioDefault3" value="pack">
                        <label class="form-check-label" for="radioDefault3">
                            Package
                        </label>
                    </div>


                </div>
                <div class="form-floating mt-3">
                    <input type="text" v-model="formdata.query" class="form-control" id="floatingQuery"
                        placeholder="Password">
                    <label for="floatingQuery">Search</label>
                </div>
                <button class="btn btn-primary mt-2" @click="search">Search</button>
            </div>
        </div>
    </div>

    <div v-if="prof_list" class="card mt-5 ms-5 me-5">
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
                            <router-link :to="`/view-professional/${prof.id}`"
                                class="btn btn-primary">View</router-link>
                        </td>
                    </tr>
                </tbody>
            </table>

        </div>
    </div>
    <div v-if="cust_list" class="card mt-5 ms-5 me-5">
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


export default {
    name: "SearchComp",

    data() {
        return {
            formdata: {
                "query_type": "prof",
                "query": ""
            },
            prof_list: null,
            cust_list: null,
            package_list: null

        }
    },
    methods: {
        async search() {
            console.log(this.formdata)
            try {
                const response = await fetch("http://localhost:5000/search", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "Authentication-Token": localStorage.getItem("token")
                    },
                    body:JSON.stringify(this.formdata)
                })
                const data = await response.json()
                if (response.status == 200) {
                    if (this.formdata.query_type =="cust") {
                        this.prof_list = null
                        this.pack_list= null
                        this.cust_list = data
                    }else if (this.formdata.query_type =="prof") {
                        this.cust_list = null
                        this.pack_list= null
                        this.prof_list = data
                        
                    }
                    else if (this.formdata.query_type =="pack") {
                        this.pack_list = data
                    }
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
    mounted() {
        // this.fetchProfessional()
        // this.fetchCustomers()
    }
}

</script>