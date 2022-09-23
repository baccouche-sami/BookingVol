

<template lang="">
    <!-- <div v-for="item of items">
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
  </div> -->
    <div class="container mx-auto sm:px-6 lg:px-8">


    <ul role="list" class="grid grid-cols-1 gap-6 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
    <li v-for="(item,index) of items" :key="index" class="col-span-1 flex flex-col divide-y divide-gray-200 rounded-lg bg-white text-center shadow">
      <div class="flex flex-1 flex-col p-8">
        <!-- <img class="mx-auto h-32 w-32 flex-shrink-0 rounded-full" src="/logo.png" alt="" />  -->
        <h3 class="mt-6 text-sm font-medium text-gray-900">Prix: <span class="ancienMontant">{{ item.montant }} €</span>  |
        <span>{{ item.montant - item.montant * 0.01 }} € </span></h3>
        <dl class="mt-1 flex flex-grow flex-col justify-between">
          <dd class="text-sm text-gray-500">Depart: {{ item.depart }}</dd>
          <dd class="text-sm text-gray-500">Arrivee: {{ item.arrive }}</dd>

          <dd class="mt-3">
            <span class="rounded-full bg-green-100 px-2 py-1 text-xs font-medium text-green-800">Promo: 10% de réduction</span> <br>
            <span class="rounded-full bg-red-100 px-2 py-1 text-xs font-medium text-white-800">Places disponible: {{ item.places }}</span>
          </dd>
        </dl>
      </div>
      <div>
        <div class="-mt-px flex divide-x divide-gray-200">
          <div class="flex w-0 flex-1">
            <a href="#" class="relative -mr-px inline-flex w-0 flex-1 items-center justify-center rounded-bl-lg border border-transparent py-4 text-sm font-medium text-gray-700 hover:text-gray-500">
              <PhoneIcon class="h-5 w-5 text-gray-400" aria-hidden="true" />
              <span class="ml-3">Book Now</span>
            </a>
          </div>
         
        </div>
      </div>
    </li>
  </ul>
    </div>
</template>
<script>
import { PhoneIcon } from '@heroicons/vue/20/solid'

export default {
  components: {
    PhoneIcon,
  },
  data() {
    return {
      items: [],
    };
  },
  async created() {
    const res = await this.$store.dispatch("fetchVols");
    console.log(res);
    this.items = res;
    res.forEach((element) => {
      this.items.push(element);
    });
  },
};
</script>
<style >

.ancienMontant {
  text-decoration: line-through;
  font-weight: 100;
}
</style>