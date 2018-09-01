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
      <b-notification type="is-danger" :active="errorMessage.length" has-icon>
        {{ errorMessage }}
      </b-notification>

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
import * as K from "../../store/constants";
export default {
  name: "VSchoolForm",
  props: ["name", "location", "district"],
  data() {
    return {
      errorMessage: ""
    };
  },
  methods: {
    saveForm() {
      let data = {
        name: this.$props.name,
        district: this.$props.district,
        location: this.$props.location
      };
      this.$store
        .dispatch(K.CREATE_SCHOOL, data)
        .then(response => {
          console.log(response);
          this.$store.dispatch(K.FETCH_SCHOOLS);
          this.$parent.close();
        })
        .catch(err => {
          this.errorMessage = err.message;
        });
    }
  }
};
</script>
