<template lang="">
  <div class="bg-white shadow sm:rounded-lg">
    <div class="px-4 py-5 sm:p-6">
      <h3 class="text-lg font-medium leading-6 text-gray-900">
        Vol #BV{{ fly.id }}
      </h3>
      <h5 class="text-md font-medium leading-6 text-gray-900">
        {{ priceVol }} 
      </h5>

      <div class="mt-2 sm:flex sm:items-start sm:justify-between">
        <div class="max-w-xl text-sm text-gray-500">
          <p>Départ : {{ fly.depart }}</p>
          <p>Destination: {{ fly.arrive }}</p>
          <p v-if="fly.source">Source: {{ fly.source }}</p>

        </div>
        
            <ButtonBook :contentType="8" :IsButton="true"  :fly="fly"/>
      </div>
    </div>

  </div>
</template>
<script>
import { mapState } from "vuex";
import ButtonBook  from "./ButtonBook.vue";

export default {
  components: {
    ButtonBook
  },
  props: {
    fly: {
      type: Object,
      default: null,
    },
  },
  computed: {
    ...mapState(["currency"]),

    priceVol(){
      return this.currency === "EURO" ? this.fly.montant +" "+ this.currency: this.fly.price_map[this.currency ==='DOLLAR' ? 'USD' : 0 ] + " "+ this.currency
    }
  }
};
</script>
<style lang=""></style>