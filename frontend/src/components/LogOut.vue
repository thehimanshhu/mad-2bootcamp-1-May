<script>
export default{
    name : "LogOut",
    methods:{
        logout(){
            localStorage.removeItem("token")
            localStorage.removeItem("role")
            this.$router.push("/login")
        }
    },
    mounted(){
        this.logout()
    }
}
</script>