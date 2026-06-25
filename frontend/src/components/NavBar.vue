<template>

    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Helpify</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto me-5">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Dashboard</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Search</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Stats</a>
                    </li>
                    <li class="nav-item">
                        <router-link to="/logout" class="nav-link btn btn-primary" href="#">LogOut</router-link>
                    </li>


                </ul>
            </div>
        </div>
    </nav>
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
    
}

</script>