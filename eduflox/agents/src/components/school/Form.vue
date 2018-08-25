<template>
<form action="">
  <div class="modal-card">
    <header class="modal-card-head">
      <p class="modal-card-title">Create New School</p>
      <a href="#" class="card-header-icon" @click.prevent="$parent.close()">
        <b-icon icon='close'/>
      </a>
    </header>
    <section class="modal-card-body">
      <b-field label="School">
        <b-input :value="name" placeholder="Name of School" required/>
      </b-field>
      <b-field label="Location">
        <b-input :value="location" placeholder="Ikeja" required/>
      </b-field>
      <b-field label="District">
        <b-input :value="district" placeholder="Lagos" required/>
      </b-field>
    </section>
    <footer class="modal-card-foot">
      <button class="button" type="button" @click="$parent.close()">Close</button>
      <button class="button is-primary" @click.prevent="saveForm">Save</button>
    </footer>
  </div>
</form>
</template>

<script>
export default {
  name: "VSchoolForm",
  props: ["name", "location", "district"],
  methods: {
    saveForm() {
      alert("saved!");
      this.$parent.close();
    }
  }
};
</script>
