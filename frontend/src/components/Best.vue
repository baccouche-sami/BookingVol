<template lang="">
  <div v-for="item of items">
    <div class="itemVol">
      <span>Depart: {{ item.depart }}</span>
      <span>Arrivee: {{ item.arrive }}</span>
      <span>Places disponible: {{ item.places }}</span>
      <span>Promo: 10% de réduction</span> 
      <div>
        Prix: <span class="ancienMontant">{{ item.montant }} €</span>  |
        <span>{{ item.montant - item.montant * 0.01 }} € </span>
      </div>  
    </div>
  </div>
  
</template>

<script>
import { defineComponent } from "vue";
export default defineComponent({
  name: "HomeComponent",
  setup() {
    const items = [];
    return {
      items,
    };
  },
  async created() {
    const res = await this.$store.dispatch("fetchVols");
    console.log(res);
    this.items = res;
    res.forEach((element) => {
      this.items.push(element); 
    });

    //appeler la methode addReservation pour enregistre une nouvelle reservation
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
.ancienMontant {
  text-decoration: line-through;
  font-weight: 100;
}
</style>