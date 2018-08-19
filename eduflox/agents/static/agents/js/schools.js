document.addEventListener("DOMContentLoaded", () => {
    new Vue({
        el: '#app',
        data: {
            schools: [],
            columns: [
                {
                    field: 'name',
                    label: 'Name',
                    sortable: true
                },
                {
                    field: 'code',
                    label: 'Code',
                    sortable: true
                },
                {
                    field: 'location',
                    label: 'Location',
                    sortable: true
                },
                {
                    field: 'district',
                    label: 'District',
                    sortable: true
                },
                {
                    field: 'status',
                    label: 'Status',
                    sortable: true
                },
                {
                    field: 'created_at',
                    label: 'Date Created',
                    sortable: true,
                    centered: true
                },
            ],
            selected: null,
            loading: false,
        },
        mounted: function () {

        },
        methods: {

        }
    })
})