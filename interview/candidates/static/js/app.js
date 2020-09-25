var app = new Vue({
    el: '#app',
    data: {
        candidates: [],
        query: ""
    },
    mounted () {
        this.loadCandidates();
    },
    methods: {
        loadCandidates () {
            axios.get('api/candidates')
                .then(response => {
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
        },
        downloadIcs(candidateId) {
            axios.get(`api/candidates/${candidateId}/ics`)
                .then(response => {
                    // handle success
                    console.log(response)
                })
                .catch(function (error) {
                    // handle error
                    console.log(error);
                })
                .then(function () {
                    // always executed
                });
        }
    },
    watch: {
        query () {
            if (this.query) {
                let url = `api/candidates?query=${this.query}`
                axios.get(url)
                    .then(response => {
                        this.candidates = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
            } else {
                this.loadCandidates()
            }
        }
    }
})
