<template>
  <div
    class="d-flex flex-wrap container-fluid justify-content-evenly pt-2"
    id="card-auto"
    style="width: 100%"
>
    <div
        id="app"
        class="card mx-2 my-4"
        v-for="app in aplicacionesTEA"
        :key="app.id"
        style="width: 18rem"
    >
        <div style="height: 200px; overflow: hidden;">
            <img
                :src="app.imagen"
                class="card-img-top"
                alt="..."
                style="max-width: 100%; height: auto; object-fit: cover;"
            />
        </div>

        <div class="card-body">
            <h5 class="card-title">{{ app.nombre }}</h5>
            <p class="card-text">
                {{ app.descripcion }}
            </p>
        </div>
        <div class="card-footer align-center">
          <a :href="app.masInformacion" target="_blank" class="btn btn-primary">Mas Información</a>
        </div>
    </div>
</div>

</template>

<script>
const aplicacionesTEA = [
  {
    id: 1,
    nombre: "GESTIAC",
    descripcion:
      "Es una aplicación para la gestión del tiempo para personas con TEA. Sirve para que comprendan de manera integrada y global tanto las actividades como el tiempo que transcurre durante las mismas.",
    masInformacion: "https://www.autismoburgos.es/conoce-nuestras-apps/",
    imagen:
      "https://autismo.org.es/wp-content/uploads/2017/05/unnamed-1536x864.png",
  },
  {
    id: 2,
    nombre: "TEMPUS",
    descripcion:
      "Es una aplicación de organización del tiempo. Te permite personalizar los pictogramas, el reloj, la música y los colores. También puedes configurar un reloj con cuenta atrás para situaciones de espera.",
    masInformacion:
      "https://autismo.org.es/nace-gestiac-una-app-gratuita-que-ayuda-la-personas-con-tea-gestionar-el-tiempo/",
    imagen:
      "http://www.autismoburgos.es/wp-content/uploads/2019/02/Screenshot_20160407-021303.png",
  },
  {
    id: 3,
    nombre: "DÍA A DÍA",
    descripcion:
      "Permite registrar las actividades como un diario visual y definir qué va a pasar en el futuro, como una agenda o planificador visual. Las actividades pueden incluir fotos, texto, vídeos y audio.",
    masInformacion: "https://fundacionorange.es/aplicaciones/dia-a-dia/",
    imagen: "https://fundacionorange.es/wp-content/uploads/2016/02/diaadia.jpg",
  },
  {
    id: 4,
    nombre: "PICTOGRAMAGENDA",
    descripcion:
      "Facilita la generación y el uso de agendas visuales. Permite configurar y ordenar una secuencia de imágenes que formarán la agenda visual.",
    masInformacion: "https://www.pictogramagenda.es/",
    imagen:
      "https://www.pictogramagenda.es/wp-content/uploads/2020/12/pictogramagenda-devices.png",
  },
  {
    id: 5,
    nombre: "NIKI AGENDA",
    descripcion:
      "Calendario visual diario/semanal. Divide el día en tres partes (mañana, tarde y noche). Cada actividad puede marcarse con un símbolo de estado (hecha, cancelada, próxima) o de tipo (preferida, programada, premiada).",
    masInformacion: "http://www.nikitalk.com/Agenda.aspx",
    imagen: "http://www.nikitalk.com/images/screens/agenda-1-es.jpg",
  },
  {
    id: 6,
    nombre: "AARLENS",
    descripcion:
      "El objetivo principal de esta iniciativa, denominada AARLENS, es tratar de conciliar a través de las nuevas tecnologías la realidad diaria con las necesidades de las personas con TEA.",
    masInformacion: "https://www.astrade.es/aarlens/",
    imagen: "https://www.astrade.es/aarlens/images/elemento_1.png",
  },
  {
    id: 7,
    nombre: "HISTORIAS ESPECIALES",
    descripcion:
      "Esta aplicación facilita la creación de tus propias historias, con texto, imágenes y sonidos. Puedes leer y escuchar tus historias, imprimirlas y compartirlas. Permite explicar tareas paso a paso.",
    masInformacion:
      "https://aulautista.com/2012/02/08/historias-especiales-special-stories/",
    imagen:
      "https://aulautista.files.wordpress.com/2012/02/foto-07-02-12-23-23-45.png?w=468&h=351",
  },
  {
    id: 8,
    nombre: "KIDS TO DO LIST",
    descripcion:
      "Con esta aplicación puedes crear fácilmente tu lista de tareas al ordenar las tarjetas de imagen. Todas las tarjetas de imagen aceptan sonidos de voz.",
    masInformacion:
      "https://play.google.com/store/apps/details?id=jp.co.litalico.kidstodolist&hl=es_419&gl=US",
    imagen:
      "https://play-lh.googleusercontent.com/QfDaGZCc6bo0FtQ3WUgCXWhsghJ4n7vkpf48zQSYRN8clli2NCM15czY0u04K9BOYYuS=w526-h296-rw",
  },
  {
    id: 9,
    nombre: "VISUAL SCHEDULE & SOCIAL STORY",
    descripcion:
      "Es una aplicación de apoyo visual virtual para ayudar a los niños y niñas con autismo y dificultades de comunicación en el hogar, la escuela y la comunidad. ",
    masInformacion:
      "https://play.google.com/store/apps/details?id=com.mts.visualscheduleandstorymaker&hl=es_419&gl=US",
    imagen:
      "https://play-lh.googleusercontent.com/AyS3acP9w_scBMnPOA-k2OkReefX5_VLhzmgBn0txdNEcSoiND1xNG2bpWFAFcZFr1wy=w526-h296-rw",
  },
  {
    id: 10,
    nombre: "SEQUENCE IT",
    descripcion:
      "Es una herramienta para fortalecer la comprensión de los procesos basados en una secuencia de eventos.",
    masInformacion:
      "https://apps.apple.com/us/app/sequence-it-create-and-arrange-sequences-for-kids/id1054793304",
    imagen:
      "https://is1-ssl.mzstatic.com/image/thumb/Purple49/v4/9c/39/ef/9c39efe9-d291-82fc-49e9-07870e9bb587/pr_source.jpg/313x0w.webp",
  },
];

export default {
  name: "Services",

  data() {
    return {
      aplicacionesTEA,
    };
  },
};
</script>

<style></style>
