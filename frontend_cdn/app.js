const app =  {
    "el" : "#my_app",
    "template" : `
        <div>
            <h1>Hello, {{name}} , Welcome to the app</h1>
        </div>
    `,
    data(){
        return {
            name : "Himanshus"
        }
    },
    
}

export default app