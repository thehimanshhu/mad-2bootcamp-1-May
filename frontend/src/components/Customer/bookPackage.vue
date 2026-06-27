<template>
    <div class="text-center mt-5">
        <h1>Book Package</h1>
    </div>
    <div class="d-flex justify-content-center mt-3">
        <div class="card " style="width: 25rem;">
            <div class="card-body">
                <div v-if="message" class="alert alert-danger mt-2 mb-3" role="alert">
                    {{ message }}
                </div>
                <div class="form-floating mb-3">
                    <input type="date" v-model="formdata.date" class="form-control" id="floatingInput"
                        placeholder="name@example.com">
                    <label for="floatingInput">Date</label>
                </div>
                <div class="form-floating">
                    <input type="time" v-model="formdata.time" class="form-control" id="floatingPassword"
                        placeholder="price">
                    <label for="floatingPrice">Time</label>
                </div>
                <button class="btn btn-primary mt-2" @click="book">Book</button>

            </div>

        </div>
    </div>

</template>

<script>
export default {
    name: "CreatePackage",
    data() {
        return {
            formdata: {
                date: "",
                time: ""
            },
            message: null,
            packId : null
        }
    },
    methods:{
        async book(){
            try {
                const response = await fetch(`http://localhost:5000/book?pack_id=${this.packId}`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json" ,
                        "Authentication-Token" : localStorage.getItem("token")
                    }, 
                    body : JSON.stringify(this.formdata)  
                })
                const data = await response.json()
                if (response.status == 200) {
                    this.$router.push("/customer/dashboard")
                    console.log(data.message)
                }
                else if (response.status == 401){
                    console.log("you are not logged in please login")
                    this.$router.push("/logout")
                }
                else if (response.status == 403){
                    console.log("you don't have access to view this resource.")
                    this.$router.push("/logout")
                }
                else if (response.status == 404){
                    
                    this.message= data.message
                    this.$router.push("/customer/dashboard")
                }
            }
            catch (error) {
                console.log(error.message)
                this.$router.go(0)
            }
        }
    },
    mounted(){
        this.packId=this.$route.params.id
    }

}

</script>