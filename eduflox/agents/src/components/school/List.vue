<template>
  <div class="columns is-multiline">
    <div id="app" class="column">
      <b-table :data="schools" :columns="columns" :selected.sync="selected" focusable></b-table>
    </div>
  </div>
</template>

<script>
export default {
    data() {
        return {
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
            loading: false
        }
    }
}
</script>
