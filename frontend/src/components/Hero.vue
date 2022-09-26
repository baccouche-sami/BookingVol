<template lang="">
  <div class="relative">
    <div class="absolute inset-x-0 bottom-0 h-1/2" />
    <div class="mx-auto max-w-7xl sm:px-6 lg:px-8">
      <div class="relative shadow-xl sm:overflow-hidden sm:rounded-2xl">
        <div class="absolute inset-0">
          <img
            class="h-full w-full object-cover"
            src="https://images.unsplash.com/photo-1511632765486-a01980e01a18?&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1908&q=80"
            alt="People working on laptops"
          />
          <div
            class="absolute inset-0 bg-gradient-to-r from-cyan-400 to-sky-500 mix-blend-multiply"
          />
        </div>
        <div class="relative px-4 py-16 sm:px-6 sm:py-24 lg:py-32 lg:px-8">
          <h1
            class="text-center text-4xl font-bold tracking-tight sm:text-5xl lg:text-6xl"
          >
            <span class="block text-white">Voyager avec</span>
            <span class="block text-blue-200">Booking Intech</span>
          </h1>
          <p
            class="mx-auto mt-6 max-w-lg text-center text-xl text-blue-200 sm:max-w-3xl"
          >
            Envolez-vous vers plus de 100 destinations à petits prix ! Trouver
            votre vol ou votre train maintenant
          </p>
          <div
            class="mx-auto mt-10 max-w-sm sm:flex sm:max-w-none sm:justify-center"
          >
            <div
              class="space-y-4 sm:mx-auto sm:inline-grid sm:grid-cols-2 sm:gap-5 sm:space-y-0"
            >
              <a
                href="#"
                @click.prevent="vol = true ; train = false;"
                class="flex items-center justify-center rounded-md border border-transparent bg-white px-4 py-3 text-base font-medium text-blue-700 shadow-sm hover:bg-blue-50 sm:px-8"
                >Trouver mon vol</a
              >
               <a
                @click.prevent="vol = false ; train = true;"
                href="#"
                class="flex items-center justify-center rounded-md border border-transparent bg-white px-4 py-3 text-base font-medium text-red-700 shadow-sm hover:bg-blue-50 sm:px-8"
                >Trouver mon train</a
              >
              <!-- <a
                href="offres"
                class="flex items-center justify-center rounded-md border border-transparent bg-blue-500 bg-opacity-60 px-4 py-3 text-base font-medium text-white shadow-sm hover:bg-opacity-70 sm:px-8"
                >Nos meilleurs Offres & Promos</a
              > -->
            </div>
          </div>
        </div>
      </div>
    </div>
    <FindVol v-show="vol" />
    <FindTrain v-show="train"/>
  </div>
</template>
<script>
import FindVol from '../components/FindVol.vue'
import FindTrain from '../components/FindTrain.vue'
export default {
  data() {
    return {
      train: false,
      vol:false
    }
  },
  components: {
    FindVol,FindTrain
  },
};
</script>
<style lang=""></style>