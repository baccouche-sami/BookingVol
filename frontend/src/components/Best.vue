<template lang="">
  <div v-for="item of items">
    <div class="itemVol">
      <span>Depart: {{ item.queryDepart }}</span>
      <span>Arrivee: {{ item.queryArrivee }}</span>
      <span>Places disponible: {{ item.nbPlaces }}</span>
      <span>Promo: {{ item.promo }}</span>   
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
export default defineComponent({
  setup() {
    const items = [
      {
        queryDepart: "CDS",
        queryDestination: "CDG",
        enabled: true,
        isOpen: false,
        selectedDepart: null,
        selectedDestination: null,
        nbPlaces: 1,
        promo: "15% de réduction",
        placesDepart: [],
        placesDestination: [],

        destination: [],
      },
      {
        queryDepart: "Paris",
        queryDestination: "Lyon",
        enabled: false,
        isOpen: false,
        selectedDepart: null,
        selectedDestination: null,
        nbPlaces: 1,
        placesDepart: [],
        placesDestination: [],

        destination: [],
      },
      {
        queryDepart: "Dallas",
        queryDestination: "Zurich",
        enabled: false,
        isOpen: false,
        selectedDepart: null,
        selectedDestination: null,
        nbPlaces: 1,
        promo: "10% de réduction",
        placesDepart: [],
        placesDestination: [],

        destination: [],
      },
      {
        queryDepart: "Madrid",
        queryDestination: "Helsinki",
        enabled: false,
        isOpen: false,
        selectedDepart: null,
        selectedDestination: null,
        nbPlaces: 1,
        promo: "20% de réduction",
        placesDepart: [],
        placesDestination: [],

        destination: [],
      },
      {
        queryDepart: "Vancouver",
        queryDestination: "Lisbon",
        enabled: false,
        isOpen: false,
        selectedDepart: null,
        selectedDestination: null,
        nbPlaces: 1,
        promo: "10% de réduction",
        placesDepart: [],
        placesDestination: [],
        destination: [],
      },
    ];
    return {
      items,
    };
  },
});
</script>
<style>
.itemVol {
  display: flex;
  flex-direction: column;
  justify-content: start;
  align-items: start;
  border: 1px solid black;
  margin: 10px;
  margin-left: 100px;
  margin-right: 100px;
  padding: 10px;
}
</style>