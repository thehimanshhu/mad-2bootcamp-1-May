<template>
    <div>
    
        <h1>{{ message }}</h1>
        <div class="">
            <router-link to="/login" type="button" class="btn btn-primary me-2">Login</router-link>
            <router-link to="/register" type="button" class="btn btn-secondary ms-2">Register</router-link>
        </div>
     

        
    </div>
</template>

<script>

export default {
    name: "HomeComp",
    data() {
        return {
            message: "Welcome to My app!",
        }
    },
   
}

</script>