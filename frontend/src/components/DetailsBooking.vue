<template lang="">
  <div>
    <p>
      <span>Détails de la reservation n° {{ id }}</span> <br />
      <span>Vol: {{ vol.depart }} --> {{ vol.arrive }}</span> <br />
      <span
        >Nom et Prénom: {{ myReservation.nom }} {{ myReservation.prenom }}</span
      >
      <br />
      <span>Nombre de passagers: {{ myReservation.nb_place }}</span> <br />
      <span>Rétour inclut: {{ myReservation.retour_inclut }} </span> <br />
      <span>Option Champagne Inclut: {{ myReservation.champagne }} </span>
      <br />
      <span
        >Montant: {{ myReservation.montant }} {{ myReservation.currency }}</span
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
        champagne: false,
        currency: "",
        montant: 0,
        retour_inclut: false,
        vol: 0,
        first_class: false,
      },
      vol: {
        depart: "",
        arrive: "",
        places: 0,
      },
    };
  },
  async created() {
    const reservation = await this.$store.dispatch("getOneBooking", this.id);
    this.myReservation = reservation;
    console.log(reservation);
    const vol = await this.$store.dispatch("getOneVol", this.myReservation.vol);
    this.vol = vol;
    console.log(vol);
  },
});
</script>
<style></style>