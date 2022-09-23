<template lang="">
  <div>
    <p>
      <span>Details de la reservation n° {{ id }}</span> <br />
      <span
        >Nom et Prenom: {{ myReservation.nom }} {{ myReservation.prenom }}</span
      >
      <br />
    </p>
  </div>
</template>

<script>
import { defineComponent } from "vue";
export default defineComponent({
  name: "DetailsBookingComponent",

  data() {
    return {
      id: this.$route.params.id,
      myReservation: {
        nom: "",
        prenom: "",
        nb_place: 0,
        optionChampagne: false,
        currency: "",
        montant: 0,
        retour_inclut: false,
        vol: 0,
        first_class: false,
      },
    };
  },
  async created() {
    const reservation = await this.$store.dispatch("getOneBooking", this.id);
    console.log(reservation);
    this.myReservation = reservation;
  },
});
</script>
<style></style>