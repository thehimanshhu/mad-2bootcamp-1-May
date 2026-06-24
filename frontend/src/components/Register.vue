<template>
    <h1>Register</h1>
    <div class="d-flex justify-content-center">

        <div class="card " style="width: 18rem;">
            <div class="card-body">
                <div v-if="message" class="alert alert-danger mt-2 mb-3" role="alert">
                    {{ message }}
                </div>

                <div class="form-floating mb-3">
                    <input type="email" v-model="formdata.email" class="form-control" id="floatingInput"
                        placeholder="name@example.com">
                    <label for="floatingInput">Email </label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" v-model="formdata.name" class="form-control" id="floatingInput"
                        placeholder="name@example.com">
                    <label for="floatingInput">Name </label>
                </div>
                <div class="form-floating mb-3">
                    <input type="password" v-model="formdata.password" class="form-control" id="floatingPassword"
                        placeholder="Password">
                    <label for="floatingPassword">Password</label>
                </div>
                <div class="form-floating">
                    <select class="form-select" v-model="formdata.role" id="floatingSelect"
                        aria-label="Floating label  select example">
                        <option value="cust">Customer</option>
                        <option value="prof">Service Provider</option>

                    </select>
                    <label for="floatingSelectDisabled">Role</label>
                </div>
                <button class="btn btn-primary mt-2" @click="register">Register</button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "RegisterComp",
    data() {
        return {
            formdata: {
                email: "",
                password: "",
                name: "",
                role: ""
            },
            message: null
        }
    },
    methods: {
        async register() {
            try {
                const response = await fetch("http://localhost:5000/register", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(this.formdata)
                })

                const data = await response.json()

                if (response.status == 200) {
                    this.$router.push("/login")
                }
                else if (response.status == 400) {
                    this.message = data.message
                }
                else if (response.status == 409) {
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