var app = new Vue({
    el: '#app',
    data: {
        candidates: []
    },
    mounted () {
        this.loadCandidates();
    },
    methods: {
        loadCandidates () {
            axios.get('api/candidates')
                .then((response) => {
                    // handle success
                    this.candidates = response.data;
                })
                .catch(function (error) {
                    // handle error
                    console.log(error);
                })
                .then(function () {
                    // always executed
                });
        }
    }
})
