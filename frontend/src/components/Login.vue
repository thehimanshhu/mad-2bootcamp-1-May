<template>
    <div class="d-flex justify-content-center">
        <div class="card " style="width: 18rem;">
            <div class="card-body">
                <div v-if="message" class="alert alert-danger mt-2 mb-3" role="alert">
                    {{ message }}
                </div>
                <div class="form-floating mb-3">
                    <input type="email" v-model="formdata.email" class="form-control" id="floatingInput" placeholder="name@example.com">
                    <label for="floatingInput">Email address</label>
                </div>
                <div class="form-floating">
                    <input type="password" v-model="formdata.password" class="form-control" id="floatingPassword" placeholder="Password">
                    <label for="floatingPassword">Password</label>
                </div>
                <button class="btn btn-primary mt-2" @click="login">Login</button>

            </div>

        </div>
    </div>

</template>

<script>
export default {
    name: "LoginComp",
    data() {
        return {
            formdata: {
                email: "",
                password: ""
            },
            message: null
        }
    },
    methods:{
        async login(){
            try {
                const response = await fetch("http://localhost:5000/login", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(this.formdata)
                })

                const data = await response.json()

                if (response.status == 200) {
                    localStorage.setItem("token" , data.token)
                    localStorage.setItem("role" , data.role)
                    if(data.role =="admin"){
                        this.$router.push("/admin/dashboard")
                    }
                    else if(data.role =="customer"){
                        this.$router.push("/customer/dashboard")
                    }
                    else if(data.role =="professionl"){
                        this.$router.push("/professional/dashboard")
                    }
                    
                }
                else if (response.status == 401) {
                    this.message = data.message
                }
                else if (response.status == 404) {
                    this.message = data.message
                }

            }
            catch (error) {
                console.log(error.message)
                this.$router.go(0)
            }
        }
    }
}

</script>